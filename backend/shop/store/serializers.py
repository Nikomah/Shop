from rest_framework import serializers
from .models import Product, Category, Subcategory, Subcat2, Subcat3, Subcat4


class CategorySerializer(serializers.ModelSerializer):
    subcategory = serializers.SerializerMethodField()

    @staticmethod
    def get_subcategory(obj):
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
    subcat2 = serializers.SerializerMethodField()

    @staticmethod
    def get_product(obj):
        prod_list = []
        prod = obj.product_set.all()
        for i in prod:
            prod_list.append(ProductSerializer(i).data)
        return prod_list

    @staticmethod
    def get_subcat2(obj):
        subcat2_list = []
        subcat2 = obj.subcat2_set.all()
        for i in subcat2:
            subcat2_list.append(Subcat2Serializer(i).data)
        return subcat2_list

    class Meta:
        model = Subcategory
        fields = ['id', 'name', 'image_url', 'product', 'subcat2']


class Subcat2Serializer(serializers.ModelSerializer):

    class Meta:
        model = Subcat2
        fields = ['id', 'name', 'image_url']


class Subcat3Serializer(serializers.ModelSerializer):

    class Meta:
        model = Subcat3
        fields = ['id', 'name', 'image_url']


class Subcat4Serializer(serializers.ModelSerializer):

    class Meta:
        model = Subcat4
        fields = ['id', 'name', 'image_url']


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'quantity', 'image_url']
