from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='dashboard'),
    path('customers/<str:pk>/', views.customers, name='customers'),
    path('products/', views.products, name='products'),
    path('create-order/<str:pk>/', views.createOrder, name='create-order'),
    path('update-order/<str:pk>/', views.updateOrder, name='update-order'),
    path('delete-order/<str:pk>/', views.deleteOrder, name='delete-order'),
]