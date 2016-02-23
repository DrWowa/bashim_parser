# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse_lazy
from django.http.response import HttpResponseRedirect
from django.views.generic import ListView, View

from .models import BashImData

from .parser import BashImParser, BashImRequest


class BashImListView(ListView):
    model = BashImData
    ordering = '-number'
    paginate_by = 10


class BashImFetchView(View):
    def get(self, *args, **kwargs):
        parser = BashImParser()
        parser.feed(BashImRequest().get_page())

        for data in parser.results:
            if not BashImData.objects.filter(number=data[0]).exists():
                BashImData(number=data[0], text=data[1]).save()

        return HttpResponseRedirect(reverse_lazy('bash_list'))
