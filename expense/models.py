from django.db import models


class Transaction(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.CharField(max_length=100)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=10, choices=(('expense', 'Expense'), ('income', 'Income')))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description

    class Meta:
        ordering = ('-date',)
        verbose_name = 'Transaction'
        verbose_name_plural = 'Transactions'


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Budget(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    month = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.month.strftime('%B %Y') + ' Budget'

    class Meta:
        verbose_name = 'Budget'
        verbose_name_plural = 'Budgets'
