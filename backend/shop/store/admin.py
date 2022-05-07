from django.contrib import admin
from .models import Category, Subcategory, Subcat2, Subcat3, Subcat4, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image_tag', 'image_url']
    list_editable = ['name']
    ordering = ['id']


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'image_tag']
    list_editable = ['name']
    list_filter = ['category']
    ordering = ['name']


@admin.register(Subcat2)
class Subcat2Admin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image_tag', 'subcategory']
    list_editable = ['name']
    ordering = ['id']


@admin.register(Subcat3)
class Subcat3Admin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image_tag', 'subcat2']
    list_editable = ['name']
    ordering = ['name']


@admin.register(Subcat4)
class Subcat4Admin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image_tag', 'subcat3']
    list_editable = ['name']
    ordering = ['name']


@admin.register(Product)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['pk', 'article', 'name', 'price', 'quantity', 'image_tag', 'image_url', 'subcategory', 'subcat2',
                    'subcat3', 'subcat4']
    list_editable = ['article', 'name', 'price', 'quantity']
    list_filter = ['subcategory', 'subcat2', 'subcat3', 'subcat4']
    ordering = ['subcategory']
