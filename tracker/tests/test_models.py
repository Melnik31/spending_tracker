import pytest
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from tracker.models import Transaction, Income

@pytest.mark.django_db #DATABASE ACCESS
def test_transaction_negative_amount():
    user = User.objects.create_user(username='testuser', password='testpass123')

    transaction = Transaction(
        slug='test-transaction',
        store='Test Store',
        amount=-50.00,  # Negative amount to test validation
        category=Transaction.CATEGORY_GROCERIES,
        owner=user
    )

    with pytest.raises(ValidationError):
        transaction.full_clean()  # This will trigger model validation

@pytest.mark.django_db #DATABASE ACCESS
def test_income_nagative_amount():
    user = User.objects.create_user(username='testuser2', password='testpass123')

    income = Income(
        source='Test Source',
        amount=-100.00,  # Negative amount to test validation
        owner=user
    )

    with pytest.raises(ValidationError):
        income.full_clean()  # This will trigger model validation
