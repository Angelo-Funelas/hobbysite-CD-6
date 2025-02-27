from django.db import models

# Create your models here.
class ProductType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    
class Product(models.Model):
    name = models.CharField(max_length=255)
    product_type = models.ForeignKey(ProductType, on_delete=models.SET_NULL, null=True, related_name="products")
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=12)