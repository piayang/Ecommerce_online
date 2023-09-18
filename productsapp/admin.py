from django.contrib import admin
from productsapp.models import Product

class ManageProduct(admin.ModelAdmin):
    list_display=['name','price','stock','istrending','img']
    list_editable=['price','stock','istrending']
    list_filter=['istrending']
    search_fields=['name','price']
    list_per_page = 5
# Register your models here. 
admin.site.register(Product,ManageProduct)