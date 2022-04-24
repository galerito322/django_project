from django.contrib import admin

from .models import Category, Recipe


class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    # escreve o slug automaticamente conforme o title
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Category, CategoryAdmin)
