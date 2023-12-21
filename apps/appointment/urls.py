from django.urls import path
from .views import ScheduleCreateAPIView, ScheduleListApiView

urlpatterns = [
    path('schedule/', ScheduleCreateAPIView.as_view(), name='place_order'),
    path('schedule/',ScheduleListApiView.as_view(), name='schedule_list')
]
