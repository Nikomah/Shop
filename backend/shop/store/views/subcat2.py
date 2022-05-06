from rest_framework import permissions
from rest_framework import viewsets

from store.models import Subcat2
from store.serializers import Subcat2Serializer


class Subcat2ViewSet(viewsets.ModelViewSet):
    queryset = Subcat2.objects.all().order_by('id')
    serializer_class = Subcat2Serializer
    permission_classes = (permissions.AllowAny,)
    pagination_class = None
