from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from main.views import index, category_detail, recipe_detail, add_recipe, update_recipe, delete_recipe

urlpatterns = [
    path('', index, name='home'),
    path('category/<str:slug>/', category_detail, name='category'),
    path('recipe-detail/<int:pk>/', recipe_detail, name='detail'),
    path('add-recipe/', add_recipe, name='add-recipe'),
    path('update-recipe/<int:pk>/', update_recipe, name='update-recipe'),
    path('delete-recipe/<int:pk>/', delete_recipe, name='delete-recipe'),
]
