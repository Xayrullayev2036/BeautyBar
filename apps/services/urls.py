from django.urls import path


from apps.services.views import ServiceList1APIView, ServiceCreateAPIView, ServiceUpdateAPIView, ServiceDeleteAPIView, \
    ServiceImageView, ServiceOwnerGetAPIView, CategoryGetAPIView


urlpatterns = [
    # path('service/api/get/<int:pk>/', ServiceList1APIView.as_view()),
    path('service/', ServiceCreateAPIView.as_view()),
    path('category/<str:type>/', CategoryGetAPIView.as_view(), name='category-list'),
    path('service/<int:pk>/', ServiceOwnerGetAPIView.as_view()),
    # path('service/<int:pk>/image', ServiceImageView.as_view(), name='service-image-upload'),
    path('service/', ServiceList1APIView.as_view()),
]