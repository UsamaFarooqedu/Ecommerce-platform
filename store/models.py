from django.db import models
from django.urls import reverse
from category.models import Category

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField()
    description = models.TextField(max_length=1000, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE )
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def get_url(self):   #Used for reverse to Product detail page from cart page
        return reverse('Product detail',args=[self.category.slug, self.slug])

    def __str__(self):
        return self.name
    
class VariationManager(models.Manager):
    def colors(self):
        return super(VariationManager, self).filter(variation_catgory = 'color')
    def sizes(self):
        return super(VariationManager, self).filter(variation_catgory = 'size')


variation_catgory_choice = (
    ('color', 'color'),
    ('size', 'size'),
)



class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variation_catgory = models.CharField(max_length=100, choices= variation_catgory_choice)
    variation_value = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now=True)

    objects = VariationManager()

    def __str__(self):
        return self.variation_value

