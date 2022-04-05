from rest_framework import serializers
from rest_framework import permissions
from store.models import Subcategory
from rest_framework import viewsets


class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = '__all__'


class SubcategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to read and modify subcategories
    """
    queryset = Subcategory.objects.all().order_by('id')
    serializer_class = SubcategorySerializer
    permission_classes = (permissions.AllowAny,)
