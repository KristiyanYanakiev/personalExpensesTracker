from django.contrib import admin
from django.contrib.admin import ModelAdmin

from categories.models import Category


# Register your models here.
@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    pass