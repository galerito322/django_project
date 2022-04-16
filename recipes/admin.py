from django.contrib import admin

from recipes.views import recipes

from .models import Category, Recipe


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    ...


admin.site.register(Category, CategoryAdmin)
