from datetime import datetime

from rest_framework import serializers

from apps.order.models import Order
from apps.services.models import Services
from apps.users.models import User
from apps.utils import get_schedule, place_order, get_duration, get_service_duration


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
    order_date = serializers.DateField()
    time_slot = serializers.CharField(max_length=5)

    def validate(self, attrs):
        request = self.context.get('request')
        user_id = request.user.id
        user_instance = User.objects.filter(id=user_id).first()

        service_inst = attrs["services"]
        order_date = attrs["order_date"]
        date = order_date.strftime("%Y-%m-%d")
        time_slot = attrs["time_slot"]
        schedule = get_schedule(service_inst)
        time = get_duration(service_inst)
        duration = get_service_duration(time)

        service_instance = Services.objects.filter(id=service_inst).first()
        place_order(schedule, date, time_slot, duration)
        print(schedule)
        print(date)
        print(time_slot)
        print(duration)

        order = Order(
            first_name=attrs['first_name'],
            last_name=attrs['last_name'],
            email=attrs['email'],
            services=service_instance,
            order_status=attrs['order_status'],
            order_date=attrs['order_date'],
            time_slot=attrs['time_slot'],
            user=user_instance
        )
        order.save()
        return attrs


class OrderRetriveSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
