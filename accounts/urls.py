from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='dashboard'),
    path('customers/<str:pk>/', views.customers, name='customers'),
    path('products/', views.products, name='products'),
    path('create-order/', views.createOrder, name='create-order'),
]