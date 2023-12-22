from django.db import models

from apps.order.choices import OrderStatusChoice
from apps.services.models import Services
from apps.users.models import User


class Order(models.Model):
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    user = models.ForeignKey(User, related_name="user_order", on_delete=models.CASCADE)
    services = models.ForeignKey(Services, related_name="services_order", on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    time_slot = models.CharField(max_length=5)
    order_status = models.CharField(choices=OrderStatusChoice.choices, max_length=255)

    class Meta:
        verbose_name = "order"
        verbose_name_plural = "orders"

    def __str__(self):
        return str(self.order_date)

# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAxNzc2OTEyLCJpYXQiOjE3MDE3Njk3MTIsImp0aSI6IjQ2MGYzYmM1ODg3ODQzNjJiNTZkNDA3NDY2ZmUwZDNhIiwidXNlcl9pZCI6MX0.-L3Oh93hK4H4z3I9iao6p1PU6jtppJgDobTz0kdJKUc
