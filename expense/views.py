from django.shortcuts import render


def index(request):
    return render(request, 'expense/form.html')


def expense(request):
    return render(request, 'expense/expense.html')
