from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('create/', views.order_create, name='order_create'),
    path('', views.order_list, name='order_list'),
    path('<int:order_id>/', views.order_detail, name='order_detail'),
    path('<int:order_id>/receipt/', views.order_receipt, name='order_receipt'),
    path('admin/', views.admin_orders, name='admin_orders'),
    path('admin/<int:order_id>/', views.admin_order_detail, name='admin_order_detail'),
    path('admin/<int:order_id>/delete/', views.admin_order_delete, name='admin_order_delete'),
] 