from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('product/', views.product, name="product"),
    path('customer/<str:cusid>/', views.customer, name="customerid"),
    path('customer/', views.customer, name="customer"),
    path('target/', views.target, name="target"),
]