from django import forms

from .models import Transaction, Income

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['store', 'amount','category']
        labels = {
            'store': 'Store Name',
            'amount': 'Amount Spent',
            'category': 'Category',
        }

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['source', 'amount']
        labels = {
            'source': 'Source of income',
            'amount': 'Income amount'
        }