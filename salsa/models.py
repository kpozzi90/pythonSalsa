# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Categories(models.Model):
    category_id = models.AutoField(primary_key=True)
    category = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'categories'


class Images(models.Model):
    image_id = models.AutoField(primary_key=True)
    recipe = models.ForeignKey('Recipes', models.DO_NOTHING, db_column='recipe', blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    alt_tag = models.TextField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    ingredient = models.ForeignKey('Ingredients', models.DO_NOTHING, db_column='ingredient', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'images'


class Ingredients(models.Model):
    ingredient_id = models.AutoField(primary_key=True)
    ingredient_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ingredients'


class IngredientsRecipesJoin(models.Model):
    ingrec_id = models.AutoField(primary_key=True)
    ingredient = models.ForeignKey(Ingredients, models.DO_NOTHING, db_column='ingredient', blank=True, null=True)
    recipe = models.ForeignKey('Recipes', models.DO_NOTHING, db_column='recipe', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ingredients_recipes_join'


class IngredientsStrings(models.Model):
    ingredstr_id = models.AutoField(primary_key=True)
    text = models.TextField(blank=True, null=True)
    recipe = models.ForeignKey('Recipes', models.DO_NOTHING, db_column='recipe', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ingredients_strings'


class Instructions(models.Model):
    instruction_id = models.AutoField(primary_key=True)
    step_number = models.IntegerField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    recipe = models.ForeignKey('Recipes', models.DO_NOTHING, db_column='recipe', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'instructions'


class Recipes(models.Model):
    recipe_id = models.AutoField(primary_key=True)
    title = models.TextField(unique=True, blank=True, null=True)
    category = models.ForeignKey(Categories, models.DO_NOTHING, db_column='category', blank=True, null=True)
    tagline = models.TextField(blank=True, null=True)
    heat = models.IntegerField(blank=True, null=True)
    yield_field = models.DecimalField(db_column='yield', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    difficulty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prep_time = models.IntegerField(blank=True, null=True)
    rating = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    votes = models.IntegerField(blank=True, null=True)
    custom = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'recipes'


class Tags(models.Model):
    tag_id = models.AutoField(primary_key=True)
    tag = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tags'


class TagsRecipeJoin(models.Model):
    tagrecipe_id = models.AutoField(primary_key=True)
    recipe = models.ForeignKey(Recipes, models.DO_NOTHING, db_column='recipe', blank=True, null=True)
    tag = models.ForeignKey(Tags, models.DO_NOTHING, db_column='tag', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tags_recipe_join'