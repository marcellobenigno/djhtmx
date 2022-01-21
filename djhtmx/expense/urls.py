from django.urls import path
from . import views as v

app_name = 'expense'

urlpatterns = [
    path('', v.expense_list, name='expense_list'),
    path('adicionar/', v.expense_create, name='expense_create'),
]