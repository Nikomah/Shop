from rest_framework import serializers
from .models import Product, Category, Subcategory, Subcat2, Subcat3, Subcat4


class CategorySerializer(serializers.ModelSerializer):
    subcategory = serializers.SerializerMethodField()

    @staticmethod
    def get_subcategory(obj):
        sub_list = []
        sub = obj.subcategory_set.all()
        for i in sub:
            sub_list.append([i.name, i.id, i.image_url])
        return sub_list

    class Meta:
        model = Category
        fields = ['id', 'name', 'image_url', 'subcategory']


class SubcategorySerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()
    subcat2 = serializers.SerializerMethodField()
    breadcrumbs = serializers.SerializerMethodField()

    @staticmethod
    def get_breadcrumbs(obj):
        return str(Category.objects.get(id=obj.category_id)).split(', ')

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
            subcat2_list.append([i.id, i.name, i.image_url])
        return subcat2_list

    class Meta:
        model = Subcategory
        fields = ['id', 'name', 'image_url', 'product', 'subcat2', 'breadcrumbs']


class Subcat2Serializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()
    subcat3 = serializers.SerializerMethodField()
    breadcrumbs = serializers.SerializerMethodField()

    @staticmethod
    def get_breadcrumbs(obj):
        return str(Subcategory.objects.select_related('category').get(id=obj.subcategory_id)).split(', ')

    @staticmethod
    def get_product(obj):
        prod_list = []
        prod = obj.product_set.all()
        for i in prod:
            prod_list.append(ProductSerializer(i).data)
        return prod_list

    @staticmethod
    def get_subcat3(obj):
        subcat3_list = []
        subcat3 = obj.subcat3_set.all()
        for i in subcat3:
            subcat3_list.append([i.id, i.name, i.image_url])
        return subcat3_list

    class Meta:
        model = Subcat2
        fields = ['id', 'name', 'image_url', 'product', 'subcat3', 'breadcrumbs']


class Subcat3Serializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()
    subcat4 = serializers.SerializerMethodField()
    breadcrumbs = serializers.SerializerMethodField()

    @staticmethod
    def get_breadcrumbs(obj):
        return str(Subcat2.objects.select_related('subcategory').get(id=obj.subcat2_id)).split(', ')

    @staticmethod
    def get_product(obj):
        prod_list = []
        prod = obj.product_set.all()
        for i in prod:
            prod_list.append(ProductSerializer(i).data)
        return prod_list

    @staticmethod
    def get_subcat4(obj):
        subcat4_list = []
        subcat4 = obj.subcat4_set.all()
        for i in subcat4:
            subcat4_list.append([i.id, i.name, i.image_url])
        return subcat4_list

    class Meta:
        model = Subcat3
        fields = ['id', 'name', 'image_url', 'product', 'subcat4', 'breadcrumbs']


class Subcat4Serializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()
    breadcrumbs = serializers.SerializerMethodField()

    @staticmethod
    def get_breadcrumbs(obj):
        return str(Subcat3.objects.select_related('subcat2').get(id=obj.subcat3_id)).split(', ')

    @staticmethod
    def get_product(obj):
        prod_list = []
        prod = obj.product_set.all()
        for i in prod:
            prod_list.append(ProductSerializer(i).data)
        return prod_list

    class Meta:
        model = Subcat4
        fields = ['id', 'name', 'image_url', 'product', 'breadcrumbs']


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'quantity', 'image_url']
