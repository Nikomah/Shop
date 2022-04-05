from rest_framework import generics
from store.models import Subcategory
from store.views.subcategory import SubcategorySerializer


class ProdInSubView(generics.ListAPIView):
    serializer_class = SubcategorySerializer

    def get_queryset(self, **kwargs):
        pk = self.kwargs.get('pk')
        subcat = Subcategory.objects.get(pk=pk)
        lst = subcat.product_set.all()
        return lst
