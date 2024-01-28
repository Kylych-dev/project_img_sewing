from rest_framework import serializers
from main_apps.apps.shirt.models import Shirt


class ShirtSerializer(serializers.ModelSerializer):
    """
    Сериализатор Рубашки
    """

    class Meta:
        model = Shirt
        fields = (
            "id",
            "name",
            "color",
            "size"
        )