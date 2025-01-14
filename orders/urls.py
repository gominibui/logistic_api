from django.urls import path
from .views import OrderListCreateView, OrderDetailView
urlpatterns = [
    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),  # GET /orders, POST /orders
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),  # GET /orders/{id}, DELETE /orders/{id}
]
