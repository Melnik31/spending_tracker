from django.shortcuts import render

from .models import Transaction

# Create your views here.
def index(request):
    return render(request, 'tracker/index.html')

def transactions(request):
    transactions = Transaction.objects.order_by('-date')
    context = {'transactions': transactions}
    return render(request, 'tracker/transactions.html', context)
