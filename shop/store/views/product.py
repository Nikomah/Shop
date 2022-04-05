from rest_framework import serializers
from store.models import Product
from rest_framework import viewsets
from rest_framework import permissions

from store.views.subcategory import SubcategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    subcategory = SubcategorySerializer()

    class Meta:
        model = Product
        fields = '__all__'


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to read and modify products
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (permissions.AllowAny,)
