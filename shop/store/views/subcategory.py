from rest_framework import permissions
from store.models import Subcategory
from rest_framework import viewsets

from store.serializers import SubcategorySerializer


class SubcategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to read and modify subcategories
    """
    queryset = Subcategory.objects.all().order_by('id')
    serializer_class = SubcategorySerializer
    permission_classes = (permissions.AllowAny,)
