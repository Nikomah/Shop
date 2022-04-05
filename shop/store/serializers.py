from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    # name = serializers.CharField(max_length=255)
    # price = serializers.DecimalField(max_digits=7, decimal_places=2)
    # quantity = serializers.IntegerField()
    # image = serializers.ImageField(read_only=True)
    # subcategory_id = serializers.IntegerField(read_only=True)
    #
    # def create(self, validated_data):
    #     return Product.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.price = validated_data.get('price', instance.price)
    #     instance.quantity = validated_data.get('quantity', instance.quantity)
    #     instance.image = validated_data.get('image', instance.image)
    #     instance.subcategory_id = validated_data.get('subcategory_id', instance.subcategory_id)
    #     instance.save()
    #     return instance
