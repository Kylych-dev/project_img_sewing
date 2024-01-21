from django.http import Http404
from drf_spectacular.utils import extend_schema, OpenApiParameter, extend_schema_view
from drf_yasg import openapi
from django.utils import timezone

from rest_framework import viewsets, status, serializers
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from apps.shirt.models import Shirt
from .serializers import ShirtSerializer
from drf_yasg.utils import swagger_auto_schema
from ..base.base_logger import MyLogger

import logging

logger = logging.getLogger(__name__)


class ShirtModelViewSet(viewsets.ModelViewSet):
    """
    Вместо определения queryset, используется метод get_queryset(), чтобы дополнительно
    настроить запрос к объектам Client, чтобы загрузить данные о складе.
    """
    serializer_class = ShirtSerializer
    # permission_classes = (IsAuthenticated, )
    permission_classes = (AllowAny, )

    # queryset = Shirt.objects.filter(is_delete=False).select_related("warehouse")
    queryset = Shirt.objects.all()


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.logger = MyLogger('shirt_api_logger', log_file='excample_cat')

        # self.logger = MyLogger('ShirtViewSet', log_file='excample_cat')

    @swagger_auto_schema(
        method='get',  # Определение HTTP-метода
        operation_description='text111',  # Описание операции
        # query_serializer=ShirtSerializer,  # Схема тела запроса
        # query_serializer=CustomQuerySerializer,  # Сериализатор для параметров запроса
        manual_parameters=[  # Ручные параметры запроса
            openapi.Parameter(
                'param_name', 
                openapi.IN_QUERY, 
                description='Description', 
                type=openapi.TYPE_STRING
                )
        ],
        operation_id='shirt_list',  # Идентификатор операции
        operation_summary='List of shirts',  # Краткое описание операции
        security=[{'api_key': []}],  # Определение безопасности
        # deprecated=True,  # Определение устаревшей операции
        responses={  # Описания ответов на запрос
            200: openapi.Response(description="Операция успешно завершена"),
            400: 'Bad Request'
        },
        # tags=['Рубашка'],  # Теги для операции
    )
    @action(detail=True, methods=["get"])
    def list(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=["post"])
    def update(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(self.get_object(), data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
        except Exception as ex:
            return Response(
                {"Сообщение": str(ex)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    @action(detail=True, methods=["post"])
    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid()
            serializer.save()
            logger.error(
                "Успешно создан клиент",
                exc_info=True,
                extra={
                'request_method': request.method,
                'request_path': request.path,
                'request_data': request.data,
                'created_client_id': serializer.data.get('id')
                }
            )
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        except Exception as ex:
            logger.error(
                f"Ошибка при создании Образца рубашки (ShirtModelViewset): {serializer}"    
	        )
            return Response(
                {"Сообщение": str(ex)},
                status=serializers.ValidationError("Illegal parameters")
            )


    @swagger_auto_schema(
        method="delete",  # Определение HTTP-метода
        operation_description='text111',  # Описание операции
        operation_id='shirt_delete',  # Идентификатор операции
        operation_summary='Delete of shirts',  # Краткое описание операции
        security=[{'api_key': []}],  # Определение безопасности
        # deprecated=True,  # Определение устаревшей операции
        responses={  # Описания ответов на запрос
            200: openapi.Response(description="Операция успешно завершена"),
            404: 'Рубашка не найдена'
        },
        tags=['Рубашка'],  # Теги для операции
    )

    @action(detail=True, methods=["delete"])
    def destroy(self, request, *args, **kwargs):
        try:
            # instance = self.get_object()
            # instance.is_delete = True   # Помечаем объект как удаленный
            # instance.save()

            self.logger.log_with_timezone("INFO", "Удаление рубашки")
            self.get_object().delete()
            self.logger.log_with_timezone("INFO", "Рубашка успешно удалена")
            return Response(
                {"Сообщение": "Рубашка удалена."},
                status=status.HTTP_204_NO_CONTENT,
            )
        
        except Http404:
            self.logger.log_with_timezone("ERROR", "Рубашка не найдена (Http404)")
            return Response(
                {"Сообщение": "Рубашка не найдена."},
                status=status.HTTP_404_NOT_FOUND,
            )
    
   
    @action(methods=["post"], detail=False)
    def multiple_create(self, request, *args, **kwargs):
        for data in request.data:
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
        return super().list(self, request, *args, **kwargs)
    # _________________________________________________________
    # @action(methods=["post"], detail=False)
    # def multiple_create2(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data, many=True)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)
    





    @action(methods=["post"], detail=False)
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)