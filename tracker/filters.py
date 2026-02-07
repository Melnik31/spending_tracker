import django_filters
from tracker.models import Transaction, Income
from django.forms import TextInput, Select, NumberInput

MONTH_CHOICES = [
    (1, 'January'),
    (2, 'February'),
    (3, 'March'),
    (4, 'April'),
    (5, 'May'),
    (6, 'June'),
    (7, 'July'),
    (8, 'August'),
    (9, 'September'),
    (10, 'October'),
    (11, 'November'),
    (12, 'December'),
]


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

    year = django_filters.NumberFilter(
        field_name='date',
        lookup_expr='year',
        label='',
        widget=NumberInput(attrs={'class': 'form-control', 'placeholder': 'Year'})
    )

    month = django_filters.ChoiceFilter(
        field_name='date',
        lookup_expr='month',
        choices=MONTH_CHOICES,
        label='',
        widget=Select(attrs={'class': 'form-select', 'placeholder': 'Month'})
    )

    class Meta:
        model = Transaction
        fields = ['category', 'store_name', 'year', 'month']
            
        

