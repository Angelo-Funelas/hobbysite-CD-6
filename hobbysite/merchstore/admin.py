from django.contrib import admin
from .models import Product, ProductType, ProductImage, Transaction

class ProductTypeAdmin(admin.ModelAdmin):
    model = ProductType
    search_fields = ("name",)

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0
class ProductAdmin(admin.ModelAdmin):
    model = Product
    search_fields = ("name",)
    list_filter = ("product_type",)
    list_display = ("name", "product_type", "price",)
    inlines = [ProductImageInline]
    
class TransactionAdmin(admin.ModelAdmin):
    model = Transaction
    search_fields = ("product", "buyer",)
    list_filter = ("status",)
    list_display = ("product", "amount", "status",)
    

admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Transaction, TransactionAdmin)
