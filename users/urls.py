from django.urls import path
from django.conf import settings
from users import views

app_name = "user"


urlpatterns = [
    path("login/",  views.login, name="login"),
    path("registration/", views.registration, name="registration"),
    path("profile/", views.profile, name="profile"),
    path("logout/", views.logout, name="logout")
]