from django.db import models
from django.utils.safestring import mark_safe


class Category(models.Model):
    objects = models.Manager
    name = models.CharField(max_length=255, verbose_name='Категория')

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    objects = models.Manager
    name = models.CharField(max_length=255, verbose_name='Подкатегория')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Подкатегории'
        verbose_name_plural = 'Подкатегории'

    def __str__(self):
        return self.name


class Product(models.Model):
    objects = models.Manager
    article = models.IntegerField(verbose_name='Артикул', null=True, blank=True)
    name = models.CharField(max_length=255, verbose_name='Наименование')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена', null=True)
    quantity = models.IntegerField(verbose_name='Количество', default=0)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, null=True, blank=True)

    @property
    def image_tag(self):
        return mark_safe('<img src=%s />' % self.image.url)

    def __str__(self):
        return f'{self.article}, {self.name}, {str(self.price)}, {str(self.quantity)}'

    class Meta:
        verbose_name = 'Товары'
        verbose_name_plural = 'Товары'
