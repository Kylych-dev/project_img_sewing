from rest_framework import serializers 
from main_apps.apps2.stock.models import Warehouse
from api.product.serializers import ProductSerializer
from api.stock.serializers import StockSerializer


class WarehouseSerializer(serializers.ModelSerializer):
    # products2 = ProductSerializer(many=True, read_only=True)
    stock = StockSerializer(many=True, source='stock_set')
    # stock = StockSerializer()

    class Meta:
        model = Warehouse
        # fields = '__all__'

        # fields = (
        #     'id',
        #     'name',
        #     'products', 
        #     'products2',
        #     # 'stock'
        # )

        fields = (
            'id',
            'name', 
            # 'products', 
            'stock'
        )


        '''
        name
        products through stock
        '''