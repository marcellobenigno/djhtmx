from django.urls import path

from . import views as v

app_name = 'state'

urlpatterns = [
    path('', v.state_list, name='state_list'),
    path('municipios-options/', v.municipality_hx_option_list, name='municipality_hx_option_list'),
    path('municipios-tr/', v.municipality_hx_tr_list, name='municipality_hx_tr_list'),
    path('regioes/', v.region_list, name='region_list'),
    path('<str:region>/', v.state_hx_list, name='state_hx_list'),
]
