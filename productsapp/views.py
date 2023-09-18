from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from productsapp.models import Product
def index(request):
    obj_product=Product.objects.filter(istrending=True) 
    return render(request,"index.html",{"products": obj_product})
def ProductDetials(request,id):
    pro_field=Product.objects.get(pk=id)
    return render(request,"detail.html",{"productfield":pro_field})

