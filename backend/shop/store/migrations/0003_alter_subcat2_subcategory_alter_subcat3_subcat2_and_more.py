# Generated by Django 4.0.3 on 2022-05-05 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_subcat2_subcat3_remove_product_category_subcat4_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcat2',
            name='subcategory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.subcategory', verbose_name='Подкатегория'),
        ),
        migrations.AlterField(
            model_name='subcat3',
            name='subcat2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.subcat2', verbose_name='Подкатегория'),
        ),
        migrations.AlterField(
            model_name='subcat4',
            name='subcat3',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.subcat3', verbose_name='Подкатегория'),
        ),
    ]
