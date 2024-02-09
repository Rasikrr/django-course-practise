from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView
from goods.models import Categories

# Create your views here.
# class Index(TemplateView):
#     template_name = "index.html"

def index(request):
    print(request.user)
    categories = Categories.objects.all()
    context = {
        "categories": categories
        }
    return render(request, "index.html", context=context)

class About(TemplateView):
    template_name = "about.html"
