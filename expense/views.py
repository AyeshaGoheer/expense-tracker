import datetime
from django.db.models import Sum, F
from django.contrib.postgres.aggregates import ArrayAgg
from django.shortcuts import render
from django.http import JsonResponse
from .models import Transaction, Budget
from django.db.models.functions import TruncDate, TruncWeek


def index(request):
    return render(request, 'expense/index.html')


def expense(request):
    current_date = datetime.date.today()
    budget = Budget.objects.filter(month__year=current_date.year, month__month=current_date.month).values('amount').first()
    transactions = Transaction.objects.annotate(
        category_name=F('category__name'),
        tag_names=ArrayAgg('tags__name')
    ).values(
        'id', 'amount', 'date', 'description', 'transaction_type', 'category_name', 'tag_names'
    ).filter(transaction_type='expense')
    transactions_this_month = transactions.filter(date__year=current_date.year, date__month=current_date.month)
    total_expense = transactions.filter(transaction_type='expense').aggregate(total=Sum('amount'))['total']
    expense_this_month = transactions_this_month.filter(transaction_type='expense').aggregate(total=Sum('amount'))['total']
    consumption = expense_this_month / budget['amount'] * 100

    daily_expenses = (
        transactions
        .annotate(tdate=TruncDate('date'))
        .values('date')
        .annotate(total_expenses=Sum('amount'))
        .order_by('date')
    )
    area_chart_data = []
    for daily_expense in daily_expenses:
        area_chart_data.append({
            'y': daily_expense['date'].strftime('%Y-%m-%d'),
            'a': float(daily_expense['total_expenses']),
        })

    weekly_expenses = (
        transactions
        .annotate(week=TruncWeek('date'))
        .values('week')
        .annotate(total_expenses=Sum('amount'))
        .order_by('-week')
    )
    line_chart_data = []
    for weekly_expense in weekly_expenses:
        line_chart_data.append({
            'y': weekly_expense['week'].strftime('%Y-%m-%d'),
            'a': float(weekly_expense['total_expenses']),
        })

    expense_by_diff_categories = transactions.filter(transaction_type='expense').values('category__name').annotate(
        total=Sum('amount'))

    donut_chart_data = []
    for expense_by_diff_category in expense_by_diff_categories:
        percentage = (expense_by_diff_category['total'] / total_expense) * 100
        donut_chart_data.append({
            'label': expense_by_diff_category['category__name'],
            'value': round(float(percentage), 1),
        })

    bar_chart_data = []
    for expense_by_diff_category in expense_by_diff_categories:
        bar_chart_data.append({
            'label': expense_by_diff_category['category__name'],
            'value': round(float(expense_by_diff_category['total']), 1),
        })

    context = {
        'budget': float(budget['amount']),
        'consumption': round(float(consumption), 1),
        'expense_this_month': float(expense_this_month),
        'total_expense': float(total_expense),
        'area_chart_data': area_chart_data,
        'line_chart_data': line_chart_data,
        'donut_chart_data': donut_chart_data,
        'bar_chart_data': bar_chart_data,
    }
    return JsonResponse(context, status=200, safe=False)
