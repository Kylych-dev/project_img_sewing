from django.http import Http404
from rest_framework.decorators import action
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from rest_framework import serializers
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from main_apps.apps3.cat.models import Cat, Owner
from .serializers import CatSerializer, OwnerSerializer
import logging
from django.utils import timezone

# from ..base.base_logger import MyLogger 

logger = logging.getLogger(__name__)
cur_time = timezone.now().strftime('%Y-%m-%d %H:%M:%S %Z')


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer


    def log_error(self, message, exception, extra_info=None):
        """
        Метод для логирования ошибок с дополнительной информацией.
        """
        extra = {
            'request_method': self.request.method,
            'request_path': self.request.path,
            'request_data': self.request.data,
        }

        if extra_info:
            extra.update(extra_info)

        logger.error(f'{message}: {exception}, время {cur_time}', exc_info=True, extra=extra)


    @swagger_auto_schema(
        method="get",
        operation_description="Список котов.",
        operation_summary="Получить список котов",
        operation_id="list_cat",
        tags=["Кот"],
        responses={
            200: openapi.Response(description="OK - Список успешно получен"),
            400: openapi.Response(description="Bad Request - Неверный запрос"),
            401: openapi.Response(description="Unauthorized - Неавторизованный запрос"),
            404: openapi.Response(description="Not Found - Ресурс не найден"),
        },
    )
    @action(detail=True, methods=["get"])
    def list(self, request, *args, **kwargs):
        try:
            cat_instance = self.get_queryset()
            serializer = self.serializer_class(cat_instance, many=True)
            # MyLogger('cat_api_logger', log_file='excample_cat').log_with_timezone("INFO", "Listing all cats")
            return Response(serializer.data)
        except Exception as e:
            # MyLogger('cat_api_logger', log_file='excample_cat').log_with_timezone("ERROR", f"Error during listing cats: {str(e)}")
            return Response(
                {"Сообщение": "Произошла ошибка при получении списка котов."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
    

    @swagger_auto_schema(
        method="get",
        operation_description="Получить кота.",
        operation_summary="Получить одного кота",
        operation_id="retrieve_cat",
        tags=["Кот"],
        responses={
            200: openapi.Response(description="OK - Кот успешно получен"),
            400: openapi.Response(description="Bad Request - Неверный запрос"),
            401: openapi.Response(description="Unauthorized - Неавторизованный запрос"),
            404: openapi.Response(description="Not Found - Ресурс не найден"),
        },
    )
    @action(detail=True, methods=["get"])
    def retrieve(self, request, *args, **kwargs):
        # serializer = self.serializer_class(self.get_object, many=True)
        cat_instance = None  # Инициализация переменной перед блоком try
        try:
            cat_instance = self.get_object()
            serializer = self.serializer_class(cat_instance)
            # MyLogger('cat_api_logger', log_file='excample_cat').log_with_timezone("INFO", f"Retrieved cat with ID: {cat_instance.id}")

            return Response(
                serializer.data,
                status=status.HTTP_200_OK
                )
        except Http404:
            # MyLogger('cat_api_logger', log_file='excample_cat').logger.log_with_timezone("ERROR", "Рубашка не найдена (Http404)")
            # MyLogger('cat_api_logger', log_file='excample_cat').log_with_timezone("ERROR", f"Retrieved cat with ID: {kwargs['pk']}")
            
            return Response(
                {"Сообщение": "Рубашка не найдена."},
                status=status.HTTP_404_NOT_FOUND,
            )
    

    @swagger_auto_schema(
        method="post",
        operation_description="Создание нового кота.",
        operation_id="create_cat",
        operation_summary="Создание кота",
        tags=["Кот"],
        # security=[{"api_key": []}],
        responses={
            201: "Created - Кот создан успешно",
            400: "Bad Request - Неверный запрос",
        },
    )
    @action(detail=True, methods=["post"])
    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            # serializer.save(warehouse=self.request.user.sewing_workshop.warehouse)
            serializer.save()
            # logger.info(f"Кот с ID {request.data} успешно создан, время---{cur_time}")
            # MyLogger('cat_api_logger', log_file='excample_cat').log_with_timezone("INFO", f"Retrieved cat with ID: {cat_instance.id}")
            # MyLogger('cat_api_logger', log_file='excample_cat').log_with_timezone("INFO", "Cat created successfully")
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        except Exception as ex:
            # MyLogger('cat_api_logger', log_file='excample_cat').log_with_timezone("ERROR", f"Error creating cat: {str(ex)}")
            return Response(
                {"Сообщение": str(ex)},
                status=status.HTTP_400_BAD_REQUEST
            )


    @swagger_auto_schema(
        method="delete",
        operation_description="Удаление кота.",
        operation_id="delete_cat",
        operation_summary="Удаление кота",
        tags=["Кот"],
        # security=[{"api_key": []}],
        # responses={
        #     201: "Created - Кот создан успешно",
        #     400: "Bad Request - Неверный запрос",
        # },
    )
    @action(detail=True, methods=["delete"])
    def destroy(self, request, *args, **kwargs):
        cat_instance = None  # Инициализация переменной перед блоком try
        try:
            cat_instance = self.get_object()
            cat_instance.delete()
            # MyLogger('cat_api_logger', log_file='excample_cat').log_with_timezone("INFO", f"Deleted cat with ID: {cat_instance.id}")
            return Response(
                {"Сообщение": "Кот успешно удален."},
                status=status.HTTP_204_NO_CONTENT
            )
        except Http404:
            # MyLogger('cat_api_logger', log_file='excample_cat').log_with_timezone("ERROR", "Рубашка не найдена (Http404)")
            return Response(
                {"Сообщение": "Рубашка не найдена."},
                status=status.HTTP_404_NOT_FOUND,
            )
        except Exception as ex:
            # MyLogger('cat_api_logger', log_file='excample_cat').log_with_timezone("ERROR", f"Error deleting cat: {str(ex)}")
            return Response(
                {"Сообщение": str(ex)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )