# Generated by Django 3.0.7 on 2020-07-13 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20200713_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='appbbc/static/images/', upload_to='gallery'),
        ),
    ]
