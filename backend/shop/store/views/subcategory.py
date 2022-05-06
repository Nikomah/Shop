from rest_framework import permissions
from rest_framework import viewsets

from store.filters import SubcategoryFilter
from store.models import Subcategory
from store.serializers import SubcategorySerializer


class SubcategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to read and modify subcategories
    """
    queryset = Subcategory.objects.all().order_by('id')
    serializer_class = SubcategorySerializer
    permission_classes = (permissions.AllowAny,)
    filter_class = SubcategoryFilter
    pagination_class = None
