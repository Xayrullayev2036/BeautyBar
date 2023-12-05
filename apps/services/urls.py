from django.urls import path

from apps.services.views import ServiceList1APIView, ServiceCreateAPIView, ServiceUpdateAPIView, ServiceDeleteAPIView, \
    ServiceImageView, ServiceListAPIView

urlpatterns = [
    path('service/api/get/<int:pk>/', ServiceList1APIView.as_view()),
    path('service/api/create/', ServiceCreateAPIView.as_view()),
    path('service/<int:pk>/image', ServiceImageView.as_view(), name='service-image-upload'),
    path('service/get/', ServiceListAPIView.as_view()),

    # path('service/api/update/<int:pk>/', ServiceUpdateAPIView.as_view()),
    # path('service/api/delete/<int:pk>', ServiceDeleteAPIView.as_view())
]


# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAxNTEzMjE0LCJpYXQiOjE3MDE1MDYwMTQsImp0aSI6ImU0ZmIwNzYzMTRiZjQyYjlhYzg2NmFhNTIwNjQwZjQ1IiwidXNlcl9pZCI6MTN9.N_-FAddygaz7eRyi7BHqiqKD6nwn0njDHxdqMJ2h014
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAxNTEzNTA3LCJpYXQiOjE3MDE1MDYzMDcsImp0aSI6ImZhMzIyN2I4NDVmNTQ3MGI5YTMwM2ZjZTQ4YjhjZjI4IiwidXNlcl9pZCI6MTR9.RBXjHI0jNSB7ZAZ4YDbo_GKQw4zyIGCNz0iGzwUxQnM