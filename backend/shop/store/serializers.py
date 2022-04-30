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
    product = serializers.SerializerMethodField()

    def get_product(self, obj):
        prod_list = []
        prod = obj.product_set.all()
        for i in prod:
            prod_list.append(ProductSerializer(i).data)
        return prod_list

    class Meta:
        model = Subcategory
        fields = ['id', 'name', 'image_url', 'product']


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'quantity', 'image_url']
