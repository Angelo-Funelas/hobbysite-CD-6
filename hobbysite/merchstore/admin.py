from django.contrib import admin
from .models import *

# Register your models here.
class ProductTyepAdmin(admin.ModelAdmin):
    model = ProductType

class ProductAdmin(admin.ModelAdmin):
    model = Product

admin.site.register(ProductType, ProductTyepAdmin)
admin.site.register(Product, ProductAdmin)