from django.contrib import admin
from .models import *

# Register your models here.

class CartAdmin(admin.ModelAdmin):
    list_display = ['cart_id', 'date']

class ItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'cart', 'quantity']

admin.site.register(Cart, CartAdmin)
admin.site.register(Items, ItemAdmin)