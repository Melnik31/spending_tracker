from django.shortcuts import render, redirect
from django.db.models import Sum

from .models import Transaction
from .forms import TransactionForm

# Create your views here.
def index(request):
    return render(request, 'tracker/index.html')

def transactions(request):
    transactions = Transaction.objects.order_by('-date')
    total_spent = Transaction.objects.aggregate(Sum('amount'))['amount__sum'] or 0
    context = {
        'transactions': transactions,
        'total_spent': total_spent,
        }
    return render(request, 'tracker/transactions.html', context)

def transaction(request, transaction_id):
    transaction = Transaction.objects.get(id=transaction_id)
    context = {'transaction': transaction}
    return render(request, 'tracker/transaction.html', context)

def add_transaction(request):
    if request.method != 'POST':
        # No data submitted; create a blank form
        form = TransactionForm()
    else:
        #POST data submitted; process data.
        form = TransactionForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect ('tracker:transactions')
        
    #Display a blank or invalid form
    context = {'form': form}
    return render(request, 'tracker/add_transaction.html', context)

def edit_transaction(request, transaction_id):
    transaction = Transaction.objects.get(id=transaction_id)

    if request.method != 'POST':
        form = TransactionForm(instance=transaction)
    else:
        form = TransactionForm(instance=transaction, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('tracker:transaction', transaction_id=transaction.id)
    context = {
            'form': form,
            'transaction': transaction,
            }
    return render(request, 'tracker/edit_transaction.html', context)

