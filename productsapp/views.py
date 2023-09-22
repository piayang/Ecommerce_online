from django.shortcuts import render
# Django page number
from django.core.paginator import Paginator
# Create your views here.
from django.http import HttpResponse
from productsapp.models import Product
def index(request):
    obj_product=Product.objects.filter(istrending=True) 
    return render(request,"index.html",{"products": obj_product})
def ProductDetials(request,id):
    pro_field=Product.objects.get(pk=id)
    return render(request,"detail.html",{"productfield":pro_field})
def all_product(request):
    allproduct=Product.objects.all().order_by("name")
    # ກຳນົດໝາຍເລກໜ້າ
    pg = request.GET.get("page")
    paginators=Paginator(allproduct,3)
    allproduct = paginators.get_page(pg)
    return render(request,"product.html",{"all_pro":allproduct})

