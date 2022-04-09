from rest_framework import viewsets
from rest_framework import permissions

from store.filters import ProductFilter
from store.models import Product
from store.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to read and modify products
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (permissions.AllowAny,)
    filterset_class = ProductFilter
