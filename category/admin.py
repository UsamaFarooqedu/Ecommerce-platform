from django.contrib import admin
from .models import *

# Register your models here.

class Categoryadmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'slug')

admin.site.register(Category, Categoryadmin)
