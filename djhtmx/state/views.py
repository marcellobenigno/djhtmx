from django.shortcuts import render

from .models import State


def state_list(request):
    template_name = 'state/state_list.html'
    regions = State.objects.values('region').distinct().order_by('region')
    context = {
        'regions': regions
    }
    return render(request, template_name, context)


def state_result(request, region):
    template_name = 'state/hx/state_hx.html'
    ufs = State.objects.filter(region__icontains=region).order_by('name')
    context = {
        'ufs': ufs
    }
    return render(request, template_name, context)
