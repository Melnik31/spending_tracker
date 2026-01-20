from django.urls import path

from . import views

app_name = 'tracker'
urlpatterns = [
    #Home page
    path('', views.index, name='index'),
    #transactions page
    path('transactions/', views.transactions, name='transactions'),
    #transaction detail page
    path('transactions/<int:transaction_id>/', views.transaction, name='transaction'),
    #Adding new transactions
    path('add_transaction/', views.add_transaction, name='add_transaction'),
    #delete trnsaction
    path('delete_transaction/<int:transaction_id>/', views.delete_transaction, name='delete_transaction'),
    #delete imcome
    path('delete_income/<int:income_id>/', views.delete_income, name='delete_income'),
    #Edit transaction
    path('edit_transaction/<int:transaction_id>/', views.edit_transaction, name='edit_transaction'),
    #Edit income
    path('edit_income/<int:income_id>/', views.edit_income, name='edit_income'),
    #incomes page
    path('incomes/', views.incomes, name='incomes'),
    #adding income
    path('add_income/', views.add_income, name='add_income'),
]
