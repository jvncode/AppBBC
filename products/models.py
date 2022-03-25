from django.db import models
from django.contrib.auth.models import User
from appbbc.settings import FUNCTIONALITIES
from django.utils.text import slugify


def upload_location(instance, filename):
    return '{}/{}'.format(instance.owner, filename)


class Category(models.Model):
    title = models.CharField(max_length=40, verbose_name='Title')
    is_active = models.BooleanField(default=False, verbose_name='Active')
    slug = models.SlugField()

    def __str__(self):
        return f'{self.title}'


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Product(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    category_bk = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Category')
    description = models.TextField(max_length=100, blank=False, null=False, default='',
                                   verbose_name='Product description')
    functionality = models.CharField(blank=True, max_length=3, choices=FUNCTIONALITIES, null=False,
                                     verbose_name='Use status')
    image = models.ImageField(blank=True, null=True, upload_to=upload_location, verbose_name='Image')
    location = models.CharField(max_length=20, blank=False, null=False, verbose_name='Location')

    def __str__(self):
        return self.description
