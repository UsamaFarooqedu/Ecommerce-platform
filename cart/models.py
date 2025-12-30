from django.db import models
from store.models import *

# Create your models here.

class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cart_id

class Items(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variation = models.ManyToManyField(Variation, blank = True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def sub_total(self):
        return self.product.price * self.quantity
    
    class Meta:
        verbose_name = 'item'
        verbose_name_plural = 'items'


    




    

    

