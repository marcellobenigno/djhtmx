from django.contrib import admin

from .models import State, Municipality


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ['name', 'initials', 'region', ]
    list_filter = ['region']
    search_fields = ['name', ]


@admin.register(Municipality)
class MunicipalityAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'cod_ibge_m', 'state',]
    list_filter = ['state__name']
    search_fields = ['name', ]
