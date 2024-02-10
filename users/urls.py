from django.urls import path
from users import views

app_name = "user"

urlpatterns = [
    path("signin/", views.signin, name="signin"),
    path("signup/", views.registration, name="signup"),
    path("profile/", views.profile, name="profile"),
    path("users-cart", views.users_cart, name="users-cart"),
    path("logout/", views.logout, name="logout"),
]