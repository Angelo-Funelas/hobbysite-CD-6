from django.contrib import admin
from .models import *

# Register your models here.
class ProductTyepAdmin(admin.ModelAdmin):
    model = ProductType
    search_fields = ("name",)

class ProductAdmin(admin.ModelAdmin):
    model = Product
    search_fields = ("name",)
    list_filter = ("product_type",)
    list_display = ("name", "product_type", "price",)

admin.site.register(ProductType, ProductTyepAdmin)
admin.site.register(Product, ProductAdmin)