# Generated by Django 3.0.7 on 2020-07-13 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200626_0015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='appbbc/static/images'),
        ),
    ]
