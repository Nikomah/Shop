# Generated by Django 4.0.3 on 2022-05-05 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subcat2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование')),
                ('image', models.ImageField(upload_to='subcat2_images')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.subcategory', verbose_name='Подкатегория')),
            ],
            options={
                'verbose_name': 'Подкатегории 2',
                'verbose_name_plural': 'Подкатегории 2',
            },
        ),
        migrations.CreateModel(
            name='Subcat3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование')),
                ('image', models.ImageField(upload_to='subcat3_images')),
                ('subcat2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.subcat2', verbose_name='Подкатегория')),
            ],
            options={
                'verbose_name': 'Подкатегории 3',
                'verbose_name_plural': 'Подкатегории 3',
            },
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.CreateModel(
            name='Subcat4',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование')),
                ('image', models.ImageField(upload_to='subcat4_images')),
                ('subcat3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.subcat3', verbose_name='Подкатегория')),
            ],
            options={
                'verbose_name': 'Подкатегории 4',
                'verbose_name_plural': 'Подкатегории 4',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='subcat2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.subcat2', verbose_name='Подкатегория 2'),
        ),
        migrations.AddField(
            model_name='product',
            name='subcat3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.subcat3', verbose_name='Подкатегория 3'),
        ),
        migrations.AddField(
            model_name='product',
            name='subcat4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.subcat4', verbose_name='Подкатегория 4'),
        ),
    ]