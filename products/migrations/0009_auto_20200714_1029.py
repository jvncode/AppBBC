# Generated by Django 3.0.7 on 2020-07-14 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20200714_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='articulos'),
        ),
    ]
