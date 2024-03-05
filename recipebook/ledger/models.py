from django.db import models
from django.urls import reverse

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self): 
        return '{}'.format(self.name)

    def get_absolute_url(self):
        return reverse('ingredients:ingredient-detail', args=[self.pk])


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return '{}'.format(self.name)

    def get_root_url(self):
        return reverse('recipes:list')

    def get_absolute_url(self):
        return reverse('recipes:recipe-detail', args=[self.pk])


class RecipeIngredient(models.Model):
    quantity = models.IntegerField()
    ingredient = models.ForeignKey(
        Ingredient, 
        on_delete=models.CASCADE,
        related_name='recipe'
    )
    recipe = models.ForeignKey(
        Recipe, 
        on_delete=models.CASCADE,
        related_name='ingredients'
    )
    
    def __str__(self): 
        return '{} - {}'.format(self.recipe.name, self.ingredient.name)

