from rest_framework import permissions
from rest_framework import viewsets

from store.models import Subcat3
from store.serializers import Subcat3Serializer


class Subcat3ViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Subcat3.objects.all().order_by('id')
    serializer_class = Subcat3Serializer
    permission_classes = (permissions.AllowAny,)
    pagination_class = None
