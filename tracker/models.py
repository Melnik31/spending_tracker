from django.db import models
from django.contrib.auth.models import User

class Transaction(models.Model):
    CATEGORY_GROCERIES = 'GR'
    CATEGORY_UTILITIES = 'UT'
    CATEGORY_ENTERTAINMENT = 'EN'
    CATEGORY_OTHER = 'OT'
    CATEGORY_CAR = 'CR'
    CATEGORY_SUBSCRIPTION = 'SB'

    CATEGORY_CHOICES = [
        (CATEGORY_GROCERIES, 'Groceries'),
        (CATEGORY_UTILITIES, 'Utilities'),
        (CATEGORY_ENTERTAINMENT, 'Entertainment'),
        (CATEGORY_OTHER, 'Other'),
        (CATEGORY_CAR, 'Car'),
        (CATEGORY_SUBSCRIPTION, 'Subscription'),
    ]
    slug = models.SlugField()
    store = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default=CATEGORY_OTHER)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    
    

    class Income(models.Model):
        source = models.CharField(max_length=100)
        amount = models.DecimalField(max_digits=10, decimal_places=2)
        owner = models.ForeignKey(User, on_delete=models.CASCADE)
