from django.urls import path
from goods import views

app_name = "catalog"

urlpatterns = [
    path("", views.catalog, name="catalog"),
    path("product/<slug:product_slug>/", views.product, name="product"),
    # path("category/<slug:cat_slug>/", views.category, name="category")
]