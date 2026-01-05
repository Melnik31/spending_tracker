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
    #Edit transaction
    path('edit_transaction/<int:transaction_id>/', views.edit_transaction, name='edit_transaction'),
]
