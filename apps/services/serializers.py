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


# Category_Get_Serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
