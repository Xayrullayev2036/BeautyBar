from django.urls import path

from apps.order.views import OrderCreateView, OrderListView, OrderUpdateView, OrderDeleteView

urlpatterns = [
    path('order/', OrderCreateView.as_view()),
    path('order/', OrderListView.as_view()),
]
