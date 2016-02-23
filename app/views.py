# -*- coding: utf-8 -*-
from django.views.generic import ListView

from .models import BashImData


class BashImListView(ListView):
    model = BashImData
    ordering = '-number'
    paginate_by = 10
