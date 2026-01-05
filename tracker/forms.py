from django import forms

from .models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['store', 'amount','category']
        labels = {
            'store': 'Store Name',
            'amount': 'Amount Spent',
            'category': 'Category',
        }