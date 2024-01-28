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

from ..base.base_logger import configure_logger

# logger = logging.getLogger(__name__)
# cur_time = timezone.now().strftime('%Y-%m-%d %H:%M:%S %Z')


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer


    # def log_error(self, message, exception, extra_info=None):
    #     """
    #     Метод для логирования ошибок с дополнительной информацией.
    #     """
    #     extra = {
    #         'request_method': self.request.method,
    #         'request_path': self.request.path,
    #         'request_data': self.request.data,
    #     }

    #     if extra_info:
    #         extra.update(extra_info)

    #     logger.error(f'{message}: {exception}, время {cur_time}', exc_info=True, extra=extra)


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
            
            # logger.info(f"Метод queryset класса **** {self.__class__.__name__} ****")
            
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
    def retrieve(self, request, *args, **kwargs):                           # */*/*/*/*/*/*/*/ current test                           
        # serializer = self.serializer_class(self.get_object, many=True)
        cat_instance = None  # Инициализация переменной перед блоком try
        try:
            cat_instance = self.get_object()
            serializer = self.serializer_class(cat_instance)
            # MyLogger('cat_api_logger', log_file='excample_cat').log_with_timezone("INFO", f"Retrieved cat with ID: {cat_instance.id}")
            # print(type(self.action), '*******')   # retrieve
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
                )
        
        except Http404 as ht:
            configure_logger().warning("Пользователь не найден", extra={"class": f"{self.__class__.__name__}.{self.action}", "error": ht})
            return Response(
                {"Сообщение": "Кот не найден."},
                status=status.HTTP_404_NOT_FOUND,
            )
    

    @swagger_auto_schema(
        method="post",
        operation_description="Создание нового кота.",
        operation_id="cat_create",
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
        responses={
            201: "Created - Кот создан успешно",
            400: "Bad Request - Неверный запрос",
        },
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
                {"Сообщение": "Кот не найден."},
                status=status.HTTP_404_NOT_FOUND,
            )
        except Exception as ex:
            # MyLogger('cat_api_logger', log_file='excample_cat').log_with_timezone("ERROR", f"Error deleting cat: {str(ex)}")
            MyLogger().log_error('Кот', kwargs['pk'], ex, __class__.__name__, self.action)
            return Response(
                {"Сообщение1111111": str(ex)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        



'''


from django.urls import path
from rest_framework.routers import DefaultRouter

from api.auth.views import RegisterView, UserAuthenticationView
from api.v1.accounts.views import CustomUserViewSet
from api.v1.sewing_workshop.views import WorkshopViewSet
from api.v1.wallet.views import WalletViewSet
from api.v1.warehouse.views import ProductViewSet, ProductTemplateViewSet
from api.v1.warehouse.material_template_views import MaterialTemplateViewSet
from api.v1.warehouse.warehousematerial_views import WarehouseMaterialViewSet
from api.v1.warehouse.warehouse_views import WarehouseViewSet
from api.v1.workorder.views import FabricationViewSet
from api.v1.order.views import OrderModelViewSet
from api.v1.client.views import ClientModelViewSet
from api.v1.cut.views import CutModelViewSet

router = DefaultRouter(trailing_slash=False)

urlpatterns = router.urls

urlpatterns.extend(
    [
        # registration
        path("register/", RegisterView.as_view({"post": "register"}), name="register"),

        # verify
        path("verify-code/", RegisterView.as_view({"post": "verify"}), name="verify"),
        path("resend/verify-code/", RegisterView.as_view({"post": "resend_verify"}), name="resend-verify"),
        
        # login
        path("login/", UserAuthenticationView.as_view({"post": "login"}), name="login"),
        path("logout/", UserAuthenticationView.as_view({"post": "logout"}), name="logout"),
        
        # user
        path("users/", CustomUserViewSet.as_view({"get": "list"}), name="user-list"),
        path("users/profile/", CustomUserViewSet.as_view({"get": "user_profile"}), name="user-profile"),
        path("users/<slug:slug>/", CustomUserViewSet.as_view({"get": "user_detail"}), name="user-detail"),
        path("users/<slug:slug>/", CustomUserViewSet.as_view({"put": "update_detail"}), name="update-detail"),
        
        # workshop
        path("workshop/", WorkshopViewSet.as_view({"get": "list"}), name="workshop-list"),
        path("workshop/<int:pk>/",WorkshopViewSet.as_view({"put": "update"}), name="workshop-update"),


        path("workshop/<int:pk>/", WorkshopViewSet.as_view({"delete": "delete"}), name="workshop-delete"),
        
        # wallet
        path("wallet/", WalletViewSet.as_view({"get": "employee_wallet"}), name="employee-wallet"),
        path("wallet/transaction/", WalletViewSet.as_view({"post": "subtract_balance"}), name="subtract-balance"),
        
        # product
        path("product/", ProductViewSet.as_view({"get": "list"}), name="product-list"),
        path("product/create/", ProductViewSet.as_view({"post": "create"}), name="product-create"),
        path("product/<int:pk>/", ProductViewSet.as_view({"put": "update"}), name="product-update"),
        path("product/<int:pk>/",ProductViewSet.as_view({"delete": "delete"}), name="product-delete"),

        
        # fabrication
        path("fabric/", FabricationViewSet.as_view({"get": "list"}), name="fabrica-list"),
        path("fabric/create/", FabricationViewSet.as_view({"post": "create"}), name="fabrica-create"),
        path("fabric/<slug:slug>/", FabricationViewSet.as_view({"put": "update"}), name="fabrica-update"),
        path("fabric/<slug:slug>/", FabricationViewSet.as_view({"delete": "delete"}), name="fabrica-delete"),
        
        # item
        path("product-template/", ProductTemplateViewSet.as_view({"get": "list"}), name="product-template-list"),
        path("product-template/create/", ProductTemplateViewSet.as_view({"post": "create"}), name="product-template-create"),
        path("product-template/<int:pk>/", ProductTemplateViewSet.as_view({"put": "update"}), name="product-template-update"),
        path("product-template/<int:pk>/", ProductTemplateViewSet.as_view({"delete": "delete"}), name="product-template-delete"),
        
        # Order
        path("order/", OrderModelViewSet.as_view({"get": "list"}), name="order-list"),
        path("order/create/", OrderModelViewSet.as_view({"post": "create"}), name="order-create"),

        path("order/create/", OrderModelViewSet.as_view({"delete": "delete"}), name="order-delete"),
        path("order/<int:pk>/", OrderModelViewSet.as_view({"put": "update"}), name="order-update"),
        
        # material
        path("material-template/", MaterialTemplateViewSet.as_view({"get": "list"}), name="material-list"),
        path("material-template/create/", MaterialTemplateViewSet.as_view({"post": "create"}), name="material-create"),
        path("material-template/<int:pk>/", MaterialTemplateViewSet.as_view({"put": "update"}), name="material-update"),
        path("material-template/<int:pk>/", MaterialTemplateViewSet.as_view({"delete": "delete"}), name="material-delete"),
        
        # warehousematerial
        path("warehousematerial/", WarehouseMaterialViewSet.as_view({"get": "list"}), name="warehousematerial-list"),
        path("warehousematerial/create/", WarehouseMaterialViewSet.as_view({"post": "create"}), name="warehousematerial-create"),
        path("warehousematerial/<int:pk>/", WarehouseMaterialViewSet.as_view({"put": "update"}),name="warehousematerial-update"),
        path("warehousematerial/<int:pk>/", WarehouseMaterialViewSet.as_view({"delete": "delete"}), name="warehousematerial-delete"),
        
        # client
        path("client/", ClientModelViewSet.as_view({"get": "list"}), name="client-list"),
        path("client/create/", ClientModelViewSet.as_view({"post": "create"}), name="client-create"),
        path("client/<int:pk>/", ClientModelViewSet.as_view({"put": "update"}), name="client-update"),
        path("client/<int:pk>/", ClientModelViewSet.as_view({"delete": "delete"}), name="client-delete"),

        # Cut
        path("cut/", CutModelViewSet.as_view({"get": "list"}), name="cut-list"),
        path("cut/create/",CutModelViewSet.as_view({"post": "create"}), name="cut-create"),
        path("cut/<int:pk>/",CutModelViewSet.as_view({"put": "update"}), name="cut-update"),
        path("cut/<int:pk>/",CutModelViewSet.as_view({"delete": "delete"}), name="cut-delete"),

        # warehouse
        path("warehouse/<int:pk>", WarehouseViewSet.as_view({"get": "retrieve"}), name="warehouse-list"),
        path("warehouse/<int:pk>", WarehouseViewSet.as_view({"delete": "delete"}), name="warehouse-delete"),
    ]
)





'''