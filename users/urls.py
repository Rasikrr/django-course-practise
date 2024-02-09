from django.urls import path
from users import views

app_name = "user"

urlpatterns = [
    path("signin/", views.signin, name="signin"),
    path("signup/", views.registration, name="signup"),
    path("logout/", views.logout, name="logout"),
    path("profile/", views.profile, name="profile")
]