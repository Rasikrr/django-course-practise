from django.urls import path
from main import views

app_name = "main"

urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("about/", views.About.as_view(), name="about")
]