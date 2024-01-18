from rest_framework.decorators import action
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from rest_framework import serializers

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from apps2.stock.models import Warehouse
from .serializers import WarehouseSerializer




class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    # queryset = Warehouse.objects.select_related('stock')
    serializer_class = WarehouseSerializer

    @swagger_auto_schema(
        method="get",
        operation_description="Список Складов.",
        # query_serializer=WarehouseSerializer,
        operation_summary="Получить список складов",
        operation_id="list_warehouse",
        tags=["Склад"],
        manual_parameters=[
            openapi.Parameter(
                "param_name",
                openapi.IN_QUERY,
                description="Описание параметра",
                type=openapi.TYPE_STRING,
            ),
        ],
        responses={
            200: openapi.Response(description="OK - Список складов успешно получен"),
            400: openapi.Response(description="Bad Request - Неверный запрос"),
            401: openapi.Response(description="Unauthorized - Неавторизованный запрос"),
            404: openapi.Response(description="Not Found - Ресурс не найден"),
        },
    )
    @action(detail=True, methods=["get"])
    def list(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.queryset, many=True)
        # serializer = self.serializer_class(self.get_object())
        return Response(serializer.data)
    


    @swagger_auto_schema(
        method="get",
        operation_description="Получить склад.",
        # query_serializer=WarehouseSerializer,
        operation_summary="Получить один склад",
        operation_id="retrieve_warehouse",
        tags=["Склад"],
        manual_parameters=[
            openapi.Parameter(
                "param_name",
                openapi.IN_QUERY,
                description="Описание параметра",
                type=openapi.TYPE_STRING,
            ),
        ],
        responses={
            200: openapi.Response(description="OK - Продукт успешно получен"),
            400: openapi.Response(description="Bad Request - Неверный запрос"),
            401: openapi.Response(description="Unauthorized - Неавторизованный запрос"),
            404: openapi.Response(description="Not Found - Ресурс не найден"),
        },
    )
    @action(detail=True, methods=["get"])
    def retrieve(self, request, *args, **kwargs):
        # serializer = self.serializer_class(self.get_object, many=True)
        # serializer = self.serializer_class(self.get_object)
        # serializer = self.serializer_class(self.get_object())
        # serializer = self.get_serializer(self.get_object())
        serializer = self.get_serializer(self.get_object())

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
            )
