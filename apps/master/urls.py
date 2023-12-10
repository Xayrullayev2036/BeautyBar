from django.urls import path
from apps.master.views import MasterRegisterCreateAPIView

urlpatterns = [
    path("master/", MasterRegisterCreateAPIView.as_view())
]
