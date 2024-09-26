from django.contrib import admin
from django.urls import path
from . import views
from api.views import AddProductView,GetProductAPIView,DeleteProductAPIView

urlpatterns=[
    path('',views.home,name='home'),
    path('addproduct/',AddProductView.as_view(),name='addproduct'),
    path('getproducts/',GetProductAPIView.as_view(),name='getproducts'),
    path('deleteproduct/<int:product_id>/',DeleteProductAPIView.as_view(),name='deleteproduct')
]