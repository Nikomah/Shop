from django_filters import rest_framework as filters

from store.models import Product, Subcategory


class ProductFilter(filters.FilterSet):
    subcategory = filters.NumberFilter()
    category = filters.NumberFilter()
    name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Product
        fields = ['category', 'name']


class SubcategoryFilter(filters.FilterSet):
    category = filters.NumberFilter()
    name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Subcategory
        fields = ['category', 'name']
