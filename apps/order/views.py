from datetime import datetime

from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response

from apps.order.models import Order
from apps.order.permissions import OrderPermission
from apps.order.serializers import OrderSerializers, OrderRetriveSerializers, OrderCreateSerializers
from apps.utils import get_schedule, get_service_duration, get_duration, place_order


class OrderCreateView(CreateAPIView):
    serializer_class = OrderCreateSerializers
    permission_classes = [OrderPermission]

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class OrderListView(ListAPIView):
    serializer_class = OrderRetriveSerializers
    permission_classes = [OrderPermission]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            if user.is_superuser:
                return Order.objects.all()
            else:
                return Order.objects.filter(user=user.id)
        else:
            raise ValidationError("Please you need to authenticate!")

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer_class = OrderSerializers
        serializer = serializer_class(queryset, many=True)
        return Response(serializer.data)


class OrderUpdateView(UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers
    permission_classes = [OrderPermission]

    def update(self, request, *args, **kwargs):
        try:
            order = self.get_object()
            serializer = self.get_serializer(order, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(user_id=self.request.user.id)
        except Order.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class OrderDeleteView(DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers
    permission_classes = [OrderPermission]

    def destroy(self, request, *args, **kwargs):
        try:
            order = self.get_object()
            self.perform_destroy(order)
            custom_message = "Order deleted successfully"
            return Response({'message': custom_message}, status=status.HTTP_204_NO_CONTENT)

        except Order.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
