from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from store.models import Product
from store.serializers import BasketSerializer, ProductSerializer


class BasketView(APIView):
    permission_classes = (AllowAny,)

    @swagger_auto_schema(request_body=BasketSerializer)
    def post(self, request):
        out = []
        for item in request.data['ids']:
            out.append(ProductSerializer(Product.objects.get(id=item)).data)
        return Response(out)
