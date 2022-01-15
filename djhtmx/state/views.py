from django.views import generic

from .models import State, Municipality


class RegionListView(generic.ListView):
    template_name = 'state/region_list.html'

    def get_queryset(self):
        return State.objects.values('region').distinct().order_by('region')


class StateListView(generic.ListView):
    template_name = 'state/state_list.html'
    model = State


class MunicipalityHXListView(generic.ListView):

    def get_queryset(self):
        return Municipality.objects.filter(
            state__pk=self.request.GET.get('state')
        )


class StateHXListView(generic.ListView):
    template_name = 'state/hx/state_hx.html'

    def get_queryset(self):
        return State.objects.filter(
            region__icontains=self.kwargs['region']
        )


region_list = RegionListView.as_view()
state_list = StateListView.as_view()

# hx
state_hx_list = StateHXListView.as_view()
municipality_hx_list = MunicipalityHXListView.as_view()
municipality_hx_option_list = MunicipalityHXListView.as_view(template_name='state/hx/municipality_hx_option.html')
municipality_hx_tr_list = MunicipalityHXListView.as_view(template_name='state/hx/municipality_hx_tr.html')
