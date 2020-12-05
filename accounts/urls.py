from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('product/', views.product, name="product"),
    path('customerid/<str:cusid>/', views.customer, name="customerid"),
    path('customer/', views.customer, name="customer"),
    path('target/', views.target, name="target"),
    path('advnum/', views.advnum, name="advnum"),
]