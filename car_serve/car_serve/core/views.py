
from django.shortcuts import render
from django.views.generic.base import TemplateView

from django.views.generic.edit import *
#from django.views.generic import *
from django.urls import *
from django.contrib.auth.models import *
from django.contrib.auth import login
from .call_form import *
from django.shortcuts import *


class Menu(TemplateView):
    template_name='home.html'
    def get_context_data(self, **kwargs):
        context = super(Menu, self).get_context_data(**kwargs)
        print("this is home model model")
        context
        return context

