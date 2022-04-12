from rest_framework import serializers
from .models import Product, Category, Subcategory


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SubcategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Subcategory
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    subcategory = SubcategorySerializer()

    class Meta:
        model = Product
        fields = ['name', 'price', 'quantity', 'image_url', 'category', 'subcategory']
