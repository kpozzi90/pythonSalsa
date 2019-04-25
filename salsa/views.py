""" define functions for the url paths to use """

import json
from django.shortcuts import render
from django.http import HttpResponse
from salsa.models import Recipes, Tags, Categories, Ingredients

def test(request):
  return HttpResponse("Hello, world. You're at the salsa index.")

def new_recipe(request):
  body = json.loads(request.body)
  print(body)
  recipe = Recipes(
    title=body['recipeName'],
    tagline = body['tagLine'],
    heat = int(body['heat']),
    yield_field = float(body['yield']),
    difficulty = int(body['difficulty']),
    prep_time = int(body['prepTime']),
    custom = body['html']
  )
  recipe.save()
  # print(recipe.objects)
  return HttpResponse('it went through')

def handle_tags(request):
  tgs = Tags.objects.all()
  print('this is tags: ', tgs)

def handle_categories(request):
  cats = Categories.objects.all()
  print('this is categories: ', cats)

def handle_ingredients(request):
  ings = Ingredients.objects.all()
  print('this is ingredients: ', ings)