from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .forms import ExpenseForm
from .models import Expense


def expense_list(request):
    template_name = 'expense/expense_list.html'
    object_list = Expense.objects.all()
    form = ExpenseForm()

    if request.POST:
        print('postou...')

    context = {
        'form': form,
        'object_list': object_list,
    }
    return render(request, template_name, context)


@require_http_methods(['POST'])
def expense_create(request):
    form = ExpenseForm(request.POST or None)

    if form.is_valid():
        expense = form.save()

    context = {'object': expense}
    return render(request, 'expense/hx/expense_hx.html', context)
