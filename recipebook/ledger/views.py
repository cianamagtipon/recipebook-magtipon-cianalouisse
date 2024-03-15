from django.shortcuts import render 
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Recipe

def index(request):
    return HttpResponse('This is the Recipe Book')


class RecipeListView(ListView):
    model = Recipe
    template_name ='recipe_list.html'
    
    
class RecipeDetailView(DetailView):
    model = Recipe
    template_name ='recipe_detail.html'