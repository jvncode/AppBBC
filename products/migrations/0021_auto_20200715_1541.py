# Generated by Django 3.0.7 on 2020-07-15 15:41

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0020_auto_20200715_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(default='', max_length=100, verbose_name='Descripción del producto'),
        ),
        migrations.AlterField(
            model_name='product',
            name='functionality',
            field=models.CharField(blank=True, choices=[('PER', 'Como nuevo y en perfecto estado de uso'), ('NOR', 'Algún deterioro pero no afecta a su funcionalidad'), ('DEF', 'Algún deterioro que afecta ligeramente a su funcionalidad')], max_length=3, verbose_name='Estado de uso'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default="'{}/{}'.format(owner,<>.jpg)", null=True, upload_to=products.models.upload_location, verbose_name='Fotografía'),
        ),
    ]
