from rest_framework import serializers
from apps.services.models import Services, Category


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = "__all__"


class ServiceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        exclude = [
            "owner"
        ]


# Category_Get_Serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
