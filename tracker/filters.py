import django_filters
from tracker.models import Transaction, Income
from django.forms import TextInput, Select, NumberInput

MONTH_CHOICES = [
    ('01', 'January'),
    ('02', 'February'),
    ('03', 'March'),
    ('04', 'April'),
    ('05', 'May'),
    ('06', 'June'),
    ('07', 'July'),
    ('08', 'August'),
    ('09', 'September'),
    ('10', 'October'),
    ('11', 'November'),
    ('12', 'December'),
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
            
        

