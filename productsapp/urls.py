from django.urls import path
from productsapp import views

urlpatterns=[
    path("",views.index),
    path("product/details/<int:id>",views.ProductDetials,name="productdetails"),
    path("allproduct",views.all_product,name="all_product"),
]