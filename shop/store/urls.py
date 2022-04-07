from django.urls import path, include

from rest_framework import routers

from store.views.category import CategoryViewSet
from store.views.prod_in_sub import ProdInSubView
from store.views.product import ProductViewSet
from store.views.sub_in_cat import SubInCatView
from store.views.subcategory import SubcategoryViewSet


router = routers.SimpleRouter()
router.register(r'product', ProductViewSet, basename='product')
router.register(r'subcategory', SubcategoryViewSet, basename='subcategory')
router.register(r'category', CategoryViewSet, basename='category')


urlpatterns = [
    path('api/v1/prod-in-sub/<int:pk>', ProdInSubView.as_view()),
    path('api/v1/sub-in-cat/<int:pk>', SubInCatView.as_view()),
    path('api/v1/', include(router.urls)),
]
