from django.urls import path
from rest_framework.routers import DefaultRouter

from api.shirt.views import ShirtModelViewSet
from api.product.views import ProductViewSet
from api.stock.views import StockViewSet
from api.warehouse.views import WarehouseViewSet
from api.cat.views import CatViewSet

router = DefaultRouter(trailing_slash=False)

urlpatterns = router.urls

urlpatterns.extend([
    # Shirt
    path("shirt/<int:pk>/", ShirtModelViewSet.as_view({"get": "retrieve"})),
    path("shirt/", ShirtModelViewSet.as_view({"get": "list"})),
    path("shirt/create/", ShirtModelViewSet.as_view({"post": "create"})),
    path(
        "shirt/<int:pk>/",
        ShirtModelViewSet.as_view(
            {
                "put": "update",
                "delete": "destroy",
            }
        ),
    ),
    path('shirt/multiple_create/', ShirtModelViewSet.as_view({'post': 'multiple_create'}), name='multiple_create'),
    path('shirt/multiple_create2/', 
         ShirtModelViewSet.as_view({'post': 'multiple_create2'}), 
         name='multiple_create2'),
    path(
        "cat/<int:pk>/",
        CatViewSet.as_view(
            {
                "post": "create",
                "delete": "destroy",
            }
        ),
    ),


    # Product
    path("product/", ProductViewSet.as_view({"get": "list"})),
    path("product/<int:pk>/get_stock/", ProductViewSet.as_view({"get": "retrieve"})),

    # path("product/create/", ProductViewSet.as_view({"post": "create"})),
    # path(
    #     "product/<slug:slug>/",
    #     ProductViewSet.as_view(
    #         {
    #             "put": "update",
    #             "delete": "delete",
    #         }
    #     ),
    # ),

    # Stock
    path("stock/", StockViewSet.as_view({"get": "list"})),
    path("stock/<int:pk>/get_stock/", StockViewSet.as_view({"get": "retrieve"})),

    # path("stock/create/", ProductViewSet.as_view({"post": "create"})),
    # path(
    #     "stock/<slug:slug>/",
    #     ProductViewSet.as_view(
    #         {
    #             "put": "update",
    #             "delete": "delete",
    #         }
    #     ),
    # ),

    # Warehouse
    path("warehouse/", WarehouseViewSet.as_view({"get": "list"})),
    path("warehouse/<int:pk>/get_stock/", WarehouseViewSet.as_view({"get": "retrieve"})),

    # path("warehouse/create/", ProductViewSet.as_view({"post": "create"})),
    # path(
    #     "warehouse/<slug:slug>/",
    #     ProductViewSet.as_view(
    #         {
    #             "put": "update",
    #             "delete": "delete",
    #         }
    #     ),
    # ),

    # Cat
    path("cat/", CatViewSet.as_view({"get": "list"})),
    path("cat/<int:pk>/get_stock/", CatViewSet.as_view({"get": "retrieve"})),
    path(
        "cat/<int:pk>/",
        CatViewSet.as_view(
            {
                "post": "create",
            }
        ),
    ),
]
)
