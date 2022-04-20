from rest_framework import serializers
from .models import Product, Category, Subcategory


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'image_url']


class SubcategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Subcategory
        fields = ['name', 'image_url']


class ProductSerializer(serializers.ModelSerializer):
    subcategory = SubcategorySerializer()
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = ['name', 'price', 'quantity', 'image_url', 'category', 'subcategory']
