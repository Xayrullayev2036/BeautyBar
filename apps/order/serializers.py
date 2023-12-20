from rest_framework import serializers

from apps.order.models import Order


class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class OrderCreateSerializers(serializers.Serializer):
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    services = serializers.IntegerField()
    order_status = serializers.CharField(max_length=20)
    order_date = serializers.DateField(format="%Y-%m-%d", required=True)
    time_slot = serializers.CharField(max_length=5)

    def create(self, validated_data):
        return Order.objects.create(**validated_data)


class OrderRetriveSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
