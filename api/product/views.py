from rest_framework.decorators import action
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from rest_framework import serializers

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from main_apps.apps2.product.models import Product
from .serializers import ProductSerializer

# from ..base import MyLogger 
from ..base import configure_logger




# import logging
# import json
# import sys

# # Настройка логгера
# logger = logging.getLogger("my_logger")
# logger.setLevel(logging.DEBUG)

# # Создание обработчика для вывода в консоль
# console_handler = logging.StreamHandler(sys.stdout)

# # Форматирование в виде JSON
# json_formatter = logging.Formatter('{"timestamp": "%(asctime)s", "level": "%(levelname)s", "message": "%(message)s"}')

# # Установка форматирования для обработчика
# console_handler.setFormatter(json_formatter)

# # Добавление обработчика к логгеру
# logger.addHandler(console_handler)

# my_logger = MyLogger().get_logger()


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @swagger_auto_schema(
        method="get",
        operation_description="Список продуктов.",
        # query_serializer=ProductSerializer,
        operation_summary="Получить список продуктов",
        operation_id="list_product",
        tags=["Продукт"],
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
    

    @swagger_auto_schema(
        method="get",
        operation_description="Получить продукт.",
        # query_serializer=ProductSerializer,
        operation_summary="Получить один продукт",
        operation_id="retrieve_product",
        tags=["Продукт"],
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
        serializer = self.serializer_class(self.get_object())
        print('start')
        # logger().warning(f'ID:{kwargs["pk"]}, class: {__class__.__name__}, method: {self.action}') # for test this fine 
        configure_logger().warning(f"Пользователь с ID ** {'user.id'} не найден", extra={"class": f"{self.__class__.__name__}.{self.action}"})
        print('end')
        
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
            )
