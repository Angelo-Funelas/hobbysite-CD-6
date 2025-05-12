from django.db import models
from django.urls import reverse
from user_management.models import Profile

class ThreadCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Thread Category'
        verbose_name_plural = 'Thread Categories'
        ordering = ["name"] # Sorted by name in ascending order

class Thread(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(ThreadCategory, on_delete=models.SET_NULL, null=True)
    entry = models.TextField()
    image = models.ImageField(upload_to='forum/images/', blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('forum:detailed_thread', args=[str(self.id)])

    class Meta:
        verbose_name = 'Thread'
        verbose_name_plural = 'Threads'
        ordering = ["-created_on"] # Sorted by creation time in descending order

class Comment(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name="forum_comments")
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name="forum_comments")
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ["created_on"] # Sorted by creation time in ascending order
