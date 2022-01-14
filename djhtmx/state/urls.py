from django.urls import path

from . import views as v

app_name = 'state'


urlpatterns = [
    path('', v.state_list, name='state_list'),
    path('<str:region>/', v.state_result, name='state_result'),
]