from django.urls import path
from goods import views

app_name = "catalog"

urlpatterns = [
    path("<slug:category_slug>/", views.catalog, name="catalog"),
    path("<slug:category_slug>/<int:page>/", views.catalog, name="catalog"),
    path("product/<slug:product_slug>/", views.product, name="product"),
]