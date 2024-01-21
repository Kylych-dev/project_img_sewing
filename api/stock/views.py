from rest_framework.decorators import action
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from rest_framework import serializers

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from apps2.stock.models import Stock
from .serializers import StockSerializer




class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

    @swagger_auto_schema(
        method="get",
        operation_description="Список Сток.",
        # query_serializer=StockSerializer,
        operation_summary="Получить список сток",
        operation_id="list_product",
        tags=["Сток"],
        manual_parameters=[
            openapi.Parameter(
                "param_name",
                openapi.IN_QUERY,
                description="Описание параметра",
                type=openapi.TYPE_STRING,
            ),
        ],
        responses={
            200: openapi.Response(description="OK - Список успешно получен"),
            400: openapi.Response(description="Bad Request - Неверный запрос"),
            401: openapi.Response(description="Unauthorized - Неавторизованный запрос"),
            404: openapi.Response(description="Not Found - Ресурс не найден"),
        },
    )
    @action(detail=True, methods=["get"])
    def list(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)