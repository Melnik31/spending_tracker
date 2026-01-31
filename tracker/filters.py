import django_filters
from tracker.models import Transaction, Income
from django.forms import TextInput, Select, NumberInput


class TransactionFilter(django_filters.FilterSet):
    category = django_filters.ChoiceFilter(
        choices=Transaction.CATEGORY_CHOICES,
        field_name='category', 
        lookup_expr='iexact',
        empty_label='All Categories',
        label='',
        widget=Select(attrs={'class': 'form-select', 'placeholder': 'Category'})
        )
    store_name = django_filters.CharFilter(
        field_name='store',
        lookup_expr='icontains',
        label='',
        widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Search by Store'})
    )

    class Meta:
        model = Transaction
        fields = {
            ('category'),
        }