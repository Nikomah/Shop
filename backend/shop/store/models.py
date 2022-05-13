from django.db import models
from django.utils.safestring import mark_safe

from shop.settings import BACKEND_URL


class Category(models.Model):
    objects = models.Manager
    name = models.CharField(max_length=255, verbose_name='Категория')
    image = models.ImageField(upload_to='cat_images/', null=True, blank=True)

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.name}, {self.pk}'

    @property
    def image_tag(self):
        return mark_safe('<img src=%s />' % (BACKEND_URL + self.image.url))

    @property
    def image_url(self):
        return BACKEND_URL + self.image.url


class Subcategory(models.Model):
    objects = models.Manager
    name = models.CharField(max_length=255, verbose_name='Подкатегория')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True,)
    image = models.ImageField(upload_to='subcat_images/', null=True, blank=True)

    class Meta:
        verbose_name = 'Подкатегории'
        verbose_name_plural = 'Подкатегории'

    def __str__(self):
        return f'{self.pk}, {self.name}, {self.category}, {self.category_id}'

    @property
    def image_tag(self):
        try:
            return mark_safe('<img src=%s />' % (BACKEND_URL + self.image.url))
        except ValueError:
            return mark_safe('<img src=%s />' % (BACKEND_URL + '/media/subcat_images/klei.png'))

    @property
    def image_url(self):
        return BACKEND_URL + self.image.url


class Subcat2(models.Model):
    objects = models.Manager
    name = models.CharField(max_length=255, verbose_name='Наименование')
    image = models.ImageField(upload_to='subcat2_images')
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, verbose_name='Подкатегория', null=True)

    class Meta:
        verbose_name = 'Подкатегории 2'
        verbose_name_plural = 'Подкатегории 2'

    def __str__(self):
        return f'{self.pk}, {self.name}, {self.subcategory}'

    @property
    def image_tag(self):
        return mark_safe('<image src=%s/>' % (BACKEND_URL + self.image.url))

    @property
    def image_url(self):
        return BACKEND_URL + self.image.url


class Subcat3(models.Model):
    objects = models.Manager
    name = models.CharField(max_length=255, verbose_name='Наименование')
    image = models.ImageField(upload_to='subcat3_images')
    subcat2 = models.ForeignKey(Subcat2, on_delete=models.CASCADE, verbose_name='Подкатегория 2', null=True)

    class Meta:
        verbose_name = 'Подкатегории 3'
        verbose_name_plural = 'Подкатегории 3'

    def __str__(self):
        return f'{self.pk}, {self.name}, {self.subcat2}'

    @property
    def image_tag(self):
        return mark_safe('<image src=%s/>' % (BACKEND_URL + self.image.url))

    @property
    def image_url(self):
        return BACKEND_URL + self.image.url


class Subcat4(models.Model):
    objects = models.Manager
    name = models.CharField(max_length=255, verbose_name='Наименование')
    image = models.ImageField(upload_to='subcat4_images')
    subcat3 = models.ForeignKey(Subcat3, on_delete=models.CASCADE, verbose_name='Подкатегория 3', null=True)

    class Meta:
        verbose_name = 'Подкатегории 4'
        verbose_name_plural = 'Подкатегории 4'

    def __str__(self):
        return {self.name}

    @property
    def image_tag(self):
        return mark_safe('<image src=%s/>' % (BACKEND_URL + self.image.url))

    @property
    def image_url(self):
        return BACKEND_URL + self.image.url


class Product(models.Model):
    objects = models.Manager
    article = models.IntegerField(verbose_name='Артикул', null=True, blank=True)
    name = models.CharField(max_length=255, verbose_name='Наименование')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена', null=True)
    quantity = models.IntegerField(verbose_name='Количество', default=0)
    image = models.ImageField(upload_to='prod_images/', null=True, blank=True)
    subcategory = models.ForeignKey(
        Subcategory, on_delete=models.CASCADE, verbose_name='Подкатегория', null=True, blank=True)
    subcat2 = models.ForeignKey(Subcat2, on_delete=models.CASCADE, verbose_name='Подкатегория 2', null=True, blank=True)
    subcat3 = models.ForeignKey(Subcat3, on_delete=models.CASCADE, verbose_name='Подкатегория 3', null=True, blank=True)
    subcat4 = models.ForeignKey(Subcat4, on_delete=models.CASCADE, verbose_name='Подкатегория 4', null=True, blank=True)

    class Meta:
        verbose_name = 'Товары'
        verbose_name_plural = 'Товары'

    @property
    def image_tag(self):
        return mark_safe('<img src=%s />' % (BACKEND_URL + self.image.url))

    @property
    def image_url(self):
        return BACKEND_URL + self.image.url

    def __str__(self):
        return f'{self.pk}, {self.name}, {str(self.price)}, {str(self.quantity)}'
