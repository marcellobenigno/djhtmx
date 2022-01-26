from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .forms import ExpenseForm
from .models import Expense


def expense_list(request):
    template_name = 'expense/expense_list.html'
    object_list = Expense.objects.all()
    form = ExpenseForm()

    context = {
        'form': form,
        'object_list': object_list,
    }
    return render(request, template_name, context)


@require_http_methods(['POST'])
def expense_create(request):
    template_name = 'expense/hx/expense_hx.html'
    form = ExpenseForm(request.POST or None)
    expense = None

    if form.is_valid():
        expense = form.save()

    context = {'object': expense}
    return render(request, template_name, context)


def expense_detail(request, pk):
    template_name = 'expense/hx/expense_detail_hx.html'
    obj = Expense.objects.get(pk=pk)
    form = ExpenseForm(request.POST or None, instance=obj)
    context = {
        'object': obj,
        'form': form,
    }
    return render(request, template_name, context)


def expense_update(request, pk):
    template_name = 'expense/hx/expense_hx.html'
    obj = Expense.objects.get(pk=pk)
    form = ExpenseForm(request.POST or None, instance=obj)

    if request.method == 'POST':
        print('post')
        print(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()

    context = {
        'object': obj,
    }

    return render(request, template_name, context)
