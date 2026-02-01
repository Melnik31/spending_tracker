from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from tracker.filters import TransactionFilter
from datetime import datetime


from .models import Transaction, Income
from .forms import TransactionForm, IncomeForm

# Create your views here.
def index(request):
    return render(request, 'tracker/index.html')

@login_required
def transactions(request):
    base_qs = Transaction.objects.filter(
        owner=request.user
    ).order_by('-date')

    transactions_filter = TransactionFilter(
        request.GET,
        queryset=base_qs
    )

    filtered_qs = transactions_filter.qs

    total_spent_filtered = filtered_qs.aggregate(
        Sum('amount')
    )['amount__sum'] or 0

    total_spent_all = base_qs.aggregate(
        Sum('amount')
    )['amount__sum'] or 0

    income = Income.objects.filter(owner=request.user).first()
    income_amount = income.amount if income else 0
    balance = income_amount - total_spent_all

    context = {
        'filter': transactions_filter,
        'transactions': filtered_qs,
        'total_spent_filtered': total_spent_filtered,
        'total_spent_all': total_spent_all,
        'balance': balance,
        }
    return render(request, 'tracker/transactions.html', context)

@login_required
def incomes(request):
    incomes = Income.objects.filter(owner=request.user).order_by('-id')
    total_income = Income.objects.filter(owner=request.user).aggregate(Sum('amount'))['amount__sum'] or 0
    context = {
        'incomes': incomes,
        'total_income': total_income,
    }
    return render(request, 'tracker/incomes.html', context)

@login_required
def transaction(request, transaction_id):
    transaction = Transaction.objects.get(id=transaction_id)
    context = {'transaction': transaction}
    return render(request, 'tracker/transaction.html', context)

@login_required
def add_transaction(request):
    if request.method != 'POST':
        # No data submitted; create a blank form
        form = TransactionForm()
    else:
        #POST data submitted; process data.
        form = TransactionForm(data=request.POST)
        if form.is_valid():
            new_transaction = form.save(commit=False)
            new_transaction.owner = request.user
            new_transaction.save()
            return redirect ('tracker:transactions')
        
    #Display a blank or invalid form
    context = {'form': form}
    return render(request, 'tracker/add_transaction.html', context)

@login_required
def delete_transaction(request, transaction_id):
    rm_transaction = get_object_or_404(Transaction, id = transaction_id)
    rm_transaction.delete()
    return redirect('tracker:transactions')

@login_required
def delete_income(request, income_id):
    rm_income = get_object_or_404(Income, id = income_id)
    rm_income.delete()
    return redirect('tracker:incomes')

@login_required
def add_income(request):
    if request.method != 'POST':
        form = IncomeForm()
    else:
        form = IncomeForm(data=request.POST)
        if form.is_valid():
            new_income = form.save(commit=False)
            new_income.owner = request.user
            new_income.save()
            return redirect('tracker:incomes')
    context = {'form': form}
    return render(request, 'tracker/add_income.html', context)

@login_required
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

@login_required
def edit_income(request, income_id):
    income = Income.objects.get(id=income_id)

    if request.method != 'POST':
        form = IncomeForm(instance=income)
    else:
        form = IncomeForm(instance=income, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('tracker:incomes')
    context = {
            'form': form,
            'income': income,
            }
    return render(request, 'tracker/edit_income.html', context)


        
        
    
