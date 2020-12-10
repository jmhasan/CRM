from django.urls import path

from . import views
from .views import APIOutletPaymentMgmtNew, MatchingSerializerView

urlpatterns = [
    path('', views.home, name="home"),
    path('product/', views.product, name="product"),
    path('customerid/<str:cusid>/', views.customer, name="customerid"),
    path('customer/', views.customer, name="customer"),
    path('target/', views.target, name="target"),
    path('advnum/', views.advnum, name="advnum"),
    path('api/matching/new', APIOutletPaymentMgmtNew.as_view(), name="advnum"),
    path('api/matching/matching', MatchingSerializerView.as_view(), name="advnum"),
]