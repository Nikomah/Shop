from django.urls import path, include
from store.views.prod_in_sub import ProdInSubView
from store.views.product import ProductViewSet
from store.views.subcategory import SubcategoryViewSet
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'product', ProductViewSet, basename='product')
router.register(r'subcategory', SubcategoryViewSet, basename='subcategory')


urlpatterns = [
    path('api/v1/prod-in-sub/<int:pk>', ProdInSubView.as_view()),
    path('api/v1/', include(router.urls)),
]
