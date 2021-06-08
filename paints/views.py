from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Paint
# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'