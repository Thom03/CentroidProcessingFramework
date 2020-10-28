from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views.generic import TemplateView


# Create your views here.

class MapPortal(TemplateView):
    template_name = "portal.html"
