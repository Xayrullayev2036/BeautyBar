from rest_framework import serializers

from apps.order.models import Order


class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class OrderCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ["user"]


class OrderRetriveSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
