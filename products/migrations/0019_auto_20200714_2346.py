# Generated by Django 3.0.7 on 2020-07-14 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_auto_20200714_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='articles/%Y/%m/%d', upload_to='articles/%Y/%m/%d', verbose_name='Fotografía'),
        ),
    ]
