from django.db import models
from django.contrib.auth.models import User
from appbbc.settings import CATEGORIES, FUNCTIONALITIES
from django.conf import settings

def upload_location(instance, filename):
    return '{}/{}'.format(instance.owner,filename)

class Product(models.Model):
    
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Usuario')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=3, choices=CATEGORIES, verbose_name='Categoría')
    description = models.TextField(max_length=100, blank=False, null=False, default='', verbose_name='Descripción del producto')
    functionality = models.CharField(blank=True, max_length=3, choices=FUNCTIONALITIES, null=False, verbose_name='Estado de uso')
    image = models.ImageField(blank=True, null=True, upload_to=upload_location, verbose_name='Fotografía')
    location = models.CharField(max_length=20, blank=False, null=False, verbose_name='Localidad')

    def __str__(self):
        return self.description
