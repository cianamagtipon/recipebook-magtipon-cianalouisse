from django.urls import path
from .views import index, recipe_book, recipe_1, recipe_2

urlpatterns=[
    path('', index, name='index'),
    path('recipes/list', recipe_book, name='recipeslist'),
    path('recipe/1', recipe_1, name='recipe1'),
    path('recipe/2', recipe_2, name='recipe2')
]

app_name='ledger'