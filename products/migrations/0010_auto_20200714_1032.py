# Generated by Django 3.0.7 on 2020-07-14 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20200714_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='media/', upload_to='articulos'),
        ),
    ]
