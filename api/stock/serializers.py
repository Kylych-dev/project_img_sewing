from rest_framework import serializers 
from apps2.stock.models import Stock
from api.product.serializers import ProductSerializer


class StockSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = Stock
        fields = (
            'id',
            'product',
            # 'warehouse', 
            'quantity',
            # 'product2'
        )
    


'''
    product
    warehouse 
    quantity 
'''