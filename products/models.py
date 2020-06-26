from django.db import models
from django.contrib.auth.models import User
from appbbc.settings import CATEGORIES

class Product(models.Model):
    
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=3, choices=CATEGORIES)
    description = models.TextField(max_length=100, blank=False, null=False, default='')
    years = models.IntegerField(blank=False, null=False)
    image = models.ImageField(upload_to='gallery', default='appbbc/static/images/no-img.jpg')
    location = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return self.description
