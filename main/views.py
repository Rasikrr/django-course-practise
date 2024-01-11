from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView

# Create your views here.
class Index(TemplateView):
    template_name = "index.html"

class About(TemplateView):
    template_name = "about.html"
