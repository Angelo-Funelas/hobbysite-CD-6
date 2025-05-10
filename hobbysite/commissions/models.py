from django.db import models
from django.urls import reverse
from user_management.models import Profile


class Commission(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('full', 'Full'),
        ('completed', 'Completed'),
        ('discontinued', 'Discontinued'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('commissions:commission_details', args=[self.pk])

    class Meta:
        ordering = ["created_on"] # Sorted by creation date in ascending order

class Job(models.Model):
    commission = models.ForeignKey(Commission, on_delete=models.CASCADE, related_name="jobs",)
    entry = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    manpower_required = models.PositiveIntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('full', 'Full'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')

    def __str__(self):
        return self.role

    class Meta:
        ordering = ["-status","-manpower_required", "role"] # Sorted by status (open>full),
        #manpower_required in descending order, role in ascending order

class JobApplication(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="job_application")
    applicant = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="applications")
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    applied_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-status', 'applied_on']
