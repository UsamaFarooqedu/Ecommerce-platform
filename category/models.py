from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    images = models.ImageField(upload_to='photos/catgories', blank=True)

    def get_url(self):
        return reverse('Product catgory', args=[self.slug])

    def __str__(self):
        return self.name
    

