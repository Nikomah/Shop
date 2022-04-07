from rest_framework.generics import ListAPIView

from store.models import Category
from store.serializers import CategorySerializer


class SubInCatView(ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self, **kwargs):
        pk = self.kwargs['pk']
        cat = Category.objects.get(pk=pk)
        subcat_in_cat = cat.subcategory_set.all()
        return subcat_in_cat
