from rest_framework import serializers 
from main_apps.apps3.cat.models import Cat, Owner


class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        # fields = [
        #     'id',
        #     # 'name', 
        #     'slug', 
        #     'description', 
        #     'price' 
        # ]
        fields = '__all__'


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        # fields = [
        #     'id',
        #     # 'name', 
        #     'slug', 
        #     'description', 
        #     'price' 
        # ]
        fields = '__all__'