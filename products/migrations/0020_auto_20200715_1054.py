# Generated by Django 3.0.7 on 2020-07-15 10:54

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_auto_20200714_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to=products.models.upload_location, verbose_name='Fotografía'),
        ),
    ]