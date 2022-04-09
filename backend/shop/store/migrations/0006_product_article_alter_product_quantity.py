# Generated by Django 4.0.3 on 2022-04-01 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_rename_products_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='article',
            field=models.IntegerField(null=True, verbose_name='Артикул'),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=0, verbose_name='Количество'),
        ),
    ]
