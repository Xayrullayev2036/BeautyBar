from rest_framework import serializers
from apps.services.models import Services, Category


class ServiceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        exclude = [
            "owner",
            "image"
        ]


class ServiceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        exclude = [
            "created_at",
            "updated_at"
        ]


class ServiceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = [
            "image"
        ]


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = "__all__"


# Category_Get_Serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "type"]


class MyQueryParamsSerializer(serializers.Serializer):
    param_name = serializers.CharField(max_length=255)
    param_value = serializers.CharField(max_length=255)
