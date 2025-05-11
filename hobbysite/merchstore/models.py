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
    STATUS_CHOICES = (
        ("available", "Available"),
        ("on_sale", "On sale"),
        ("out_of_stock", "Out of stock"),
    )
    status = models.CharField(max_length=32, choices=STATUS_CHOICES, default="Available")
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("merchstore:item", kwargs={"id": self.id})
    
    def update_status(self):
        if self.stock <= 0:
            self.status = "out_of_stock"
        else:
            self.status = "available"
        self.save()
        
    def purchase(self, profile, qty, status):
        if self.stock < qty:
            raise ValueError("Out of stock.")
        if self.owner == profile:
            raise ValueError("You can't purchase your own product.")
        self.stock -= qty
        self.save()
        self.update_status()
    
    class Meta:
        ordering = ["name"] # order by name ascending order

class Transaction(models.Model):
    buyer = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name="purchases")
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name="purchases")
    amount = models.PositiveIntegerField()
    STATUS_CHOICES = (
        ("on_cart", "On Cart"),
        ("to_pay", "To Pay"),
        ("to_ship", "To Ship"),
        ("to_receive", "To Receive"),
        ("delievered", "Delivered"),
    )
    status = models.CharField(max_length=32, choices=STATUS_CHOICES)
    created_on = models.DateTimeField(auto_now_add=True)