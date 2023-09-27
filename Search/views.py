import json

from django.shortcuts import render
from django.views.generic import ListView

from Search.models import Info


class InfoListView(ListView):
    model = Info
    template_name = 'Search/main.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs_json"] = json.dumps(list(Info.objects.values()))
        return context
