from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    display_name = models.CharField(max_length=63)
    email_address = models.EmailField()
    profile_picture = models.ImageField(blank=True, upload_to='profile_pictures/', default='profile_pictures/default.png')
    def __str__(self):
        return self.display_name