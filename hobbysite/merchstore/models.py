from django.db import models
from django.urls import reverse
from user_management.models import Profile

class ProductType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["name"] # order by name ascending order
    
class Product(models.Model):
    name = models.CharField(max_length=255)
    product_type = models.ForeignKey(ProductType, on_delete=models.SET_NULL, null=True, related_name="products")
    stock = models.PositiveIntegerField(default=0)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="products")
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=12)
    status = models.CharField(max_length=32, default="Available")
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("merchstore:item", kwargs={"id": self.id})
    
    def update_stock(self, new_stock):
        self.stock = int(new_stock)
        if self.stock <= 0:
            self.status = "Out of stock"
        else:
            self.status = "Available"
        self.save()
    
    class Meta:
        ordering = ["name"] # order by name ascending order

class Transaction(models.Model):
    buyer = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name="purchases")
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name="purchases")
    amount = models.PositiveIntegerField()
    status = models.CharField(max_length=32)
    created_on = models.DateTimeField(auto_now_add=True)