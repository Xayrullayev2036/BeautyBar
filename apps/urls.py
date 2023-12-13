from django.urls import path, include

urlpatterns = [
    path('', include("apps.users.urls")),
    path('', include("apps.order.urls")),
    path('', include('apps.core.urls')),
    path('', include('apps.services.urls')),
    path('', include('apps.master.urls')),
    path('', include('apps.appointment.urls'))
]
