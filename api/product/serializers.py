from rest_framework import serializers 
from apps2.product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            # 'name', 
            'slug', 
            'description', 
            'price' 
        ]
        # fields = '__all__'
    





        '''
        name 
        slug 
        description 
        price 

        created 
        updated
        '''