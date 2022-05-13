from rest_framework import viewsets, permissions

from store.models import Category
from store.serializers import CategorySerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer
    permission_classes = (permissions.AllowAny,)
    pagination_class = None
