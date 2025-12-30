from django.contrib import admin
from .models import *

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug" : ("name",)} # Used for auto genrated slug 
    list_display = ('name','price','stock','category','slug','created_at')

admin.site.register(Product, ProductAdmin)

class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_catgory', 'variation_value', 'created_date')

admin.site.register(Variation, VariationAdmin)