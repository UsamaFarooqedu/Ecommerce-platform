from django.db import models

# Create your models here.

class category(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=True)
    slug = models.CharField(max_length=200, unique=True)
    images = models.ImageField(upload_to='\photos', blank=True)

    def __str__(self):
        return self.name
    

