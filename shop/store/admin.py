from django.contrib import admin
from .models import Category, Subcategory, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_editable = ['name']
    ordering = ['id']

    list_display_links = None


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category']
    list_editable = ['name']
    ordering = ['name']
    list_display_links = None


@admin.register(Product)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['pk', 'article', 'name', 'price', 'quantity', 'image_tag', 'subcategory', 'category']
    list_editable = ['article', 'name', 'price', 'quantity']
    ordering = ['subcategory']
    list_display_links = None
