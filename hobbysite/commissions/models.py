from django.db import models
from django.urls import reverse

# Create your models here.
class Commission(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    people_required = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('commissions:commission_details', args=[self.pk])

    class Meta:
        ordering = ["created_on"] # Sorted by creation date in ascending order

class Comment(models.Model):
    commission = models.ForeignKey(Commission, on_delete=models.CASCADE, related_name="comments",)
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment from {self.commission.title} on {self.created_on.strftime('%d-%m-%Y')}"

    class Meta:
        ordering = ["-created_on"] # Sorted by creation date in descending order
