from rest_framework import serializers
from .models import Product, Category, Subcategory


class CategorySerializer(serializers.ModelSerializer):
    subcategory = serializers.SerializerMethodField()

    def get_subcategory(self, obj):
        sub_list = []
        sub = obj.subcategory_set.all()
        for i in sub:
            sub_list.append(SubcategorySerializer(i).data)
        return sub_list

    class Meta:
        model = Category
        fields = ['id', 'name', 'image_url', 'subcategory']


class SubcategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Subcategory
        fields = ['id', 'name', 'image_url']


class ProductSerializer(serializers.ModelSerializer):
    subcategory = SubcategorySerializer()
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = ['name', 'price', 'quantity', 'image_url', 'category', 'subcategory']
