""" define functions for the url paths to use """

import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from salsa.models import Recipes, Tags, Categories, Ingredients, Images, Instructions

def new_recipe(request):
  body = json.loads(request.body)
  print(body)
  category = Categories.objects.get(pk = body['category'])
  new_recipe = Recipes(
    title=body['recipeName'],
    category=category,
    tagline = body['tagLine'],
    heat = int(body['heat']),
    yield_field = float(body['yield']),
    difficulty = int(body['difficulty']),
    prep_time = int(body['prepTime']),
    custom = body['html']
  )
  new_recipe.save()
  # img_list = []
  # for i in range(len(body['images'])):
  #   image = body['images'][i]
  #   img_list.append(
  #     Images(recipe = new_recipe, 
  #     url = image['url'], 
  #     alt_tag = image['altTag'], 
  #     height = image['height'], 
  #     width = image['width'],
  #     type = 1 if i == 0 else 2
  #     position = None if i == 0 else i
  #     ))
  # Images.objects.bulk_create(img_list)
  instructions_list = []
  for i in range(len(body['instructions'])):
    instruction = body['instructions'][i]
    instructions_list.append(
      Instructions(
      step_number = i + 1,
      test = instruction['instruction'],
      recipe = new_recipe
      ))
  Instructions.objects.bulk_create(instructions_list)

  # print(recipe.objects)
  return HttpResponse('it went through')

def handle_tags(request):
  if request.method == 'GET':
    tgs = list(Tags.objects.values())
    return JsonResponse(tgs, safe=False)
  elif request.method == 'POST':
    body = json.loads(request.body)
    new_tag = Tags(tag = body['tag'])
    new_tag.save()
    return HttpResponse('saved')


def handle_categories(request):
  if request.method == 'GET':
    cats = list(Categories.objects.values())
    return JsonResponse(cats, safe=False)
  elif request.method == 'POST':
    body = json.loads(request.body)
    new_cat = Categories(category = body['category'])
    new_cat.save()
    return HttpResponse('saved')

def handle_ingredients(request):
  if request.method == 'GET':
    ings = list(Ingredients.objects.values())
    return JsonResponse(ings, safe=False)
  elif request.method == 'POST':
    body = json.loads(request.body)
    new_ing = Ingredients(ingredient_name = body['ingredient'])
    new_ing.save()
    key = new_ing.pk
    new_img = Images(ingredient = new_ing, url = body['url'], alt_tag = body['altTag'], height = body['height'], width = body['width'])
    new_img.save()
    return HttpResponse('saved')