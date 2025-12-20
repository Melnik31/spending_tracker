from django.urls import path

from . import views

app_name = 'tracker'
urlpatterns = [
    #Home page
    path('', views.index, name='index'),
    #transactions page
    path('transactions/', views.transactions, name='transactions'),
]
