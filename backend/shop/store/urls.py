from django.urls import path, include

from rest_framework import routers

from store.views.basket import BasketView
from store.views.category import CategoryViewSet
from store.views.product import ProductViewSet
from store.views.subcat2 import Subcat2ViewSet
from store.views.subcat3 import Subcat3ViewSet
from store.views.subcat4 import Subcat4ViewSet
from store.views.subcategory import SubcategoryViewSet


router = routers.SimpleRouter()
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'subcategory', SubcategoryViewSet, basename='subcategory')
router.register(r'subcat2', Subcat2ViewSet, basename='subcat2')
router.register(r'subcat3', Subcat3ViewSet, basename='subcat3')
router.register(r'subcat4', Subcat4ViewSet, basename='subcat4')
router.register(r'product', ProductViewSet, basename='product')


urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/basket', BasketView.as_view(), name='basket'),
]
