from django.db import models

# Create your models here.
class Commission(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()
    peopleRequired = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["created_on"] # Sorted by creation date in ascending order

class Comment(models.Model):
    commission = models.ForeignKey(
        Commission,
        on_delete=models.CASCADE, 
        related_name="comments",
    )
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f"Comment from {self.commission.title} on {self.createdOn.strftime(%d-%m-%Y)}"

    class Meta:
        ordering = ["-created_on"] # Sorted by creation date in descending order