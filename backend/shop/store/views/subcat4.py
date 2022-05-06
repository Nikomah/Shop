from rest_framework import permissions
from rest_framework import viewsets

from store.models import Subcat4
from store.serializers import Subcat4Serializer


class Subcat4ViewSet(viewsets.ModelViewSet):
    queryset = Subcat4.objects.all().order_by('id')
    serializer_class = Subcat4Serializer
    permission_classes = (permissions.AllowAny,)
    pagination_class = None
