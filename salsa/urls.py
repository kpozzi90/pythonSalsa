from django.urls import path

from . import views

urlpatterns = [
    path('newRecipe', views.new_recipe, name='newRecipe'),
    path('handleTags', views.handle_tags, name='getTags'),
    path('handleCategories', views.handle_categories, name='getCategories'),
    path('handleIngredients', views.handle_ingredients, name='getCategories'),
]
