from django.urls import path
from . import views

urlpatterns = [
    # App
    path("", views.Home, name="frontpage"),
    path("orders/<str:pk>", views.Orders, name="orders"),
    path("food-search/", views.FoodSearch, name="search"),
    path("foods/", views.Foods, name="food"),
    path("categories/", views.Categories, name="categories"),
    path("category-food/", views.CategoryFoods, name="category-food"),
]
