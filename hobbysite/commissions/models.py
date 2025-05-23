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
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('commissions:commission_details', args=[self.id])

    class Meta:
        verbose_name = 'Commission'
        verbose_name_plural = 'Commissions'
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
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'
        ordering = ["-status","-manpower_required", "role"] #sorted by status (Open > Full), 
        #manpower required, in descending order, then role, in ascending order

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
        verbose_name = 'Job Application'
        verbose_name_plural = 'Job Applications'
        ordering = ['applied_on']# sorted by status (Pending first, then Accepted, then Rejected), 
        #then Applied On, in descending order. Custom sorting for status is under admin.py.

