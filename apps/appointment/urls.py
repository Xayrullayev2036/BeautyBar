from django.urls import path
from .views import ScheduleCreateAPIView

urlpatterns = [
    path('Schedule/', ScheduleCreateAPIView.as_view(), name='place_order'),
]
