from django.urls import path
from . import views as v

app_name = 'expense'

urlpatterns = [
    path('', v.expense_list, name='expense_list'),
    path('adicionar/', v.expense_create, name='expense_create'),
    path('<int:pk>/', v.expense_detail, name='expense_detail'),
    path('<int:pk>/editar/', v.expense_update, name='expense_update'),
]
