from django.db import models
from django.urls import reverse
from user_management.models import Profile

class ThreadCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

    # This function gets the latest created within the category by accessing the foreign key connected to the Post model.
    def latest_thread(self):
        return self.threads.order_by('-created_on')[0]

    class Meta:
        verbose_name = 'Thread Category'
        verbose_name_plural = 'Thread Categories'
        ordering = ["name"]

class Thread(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(ThreadCategory, on_delete=models.SET_NULL, null=True, related_name="threads")
    entry = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('forum:detailed_thread', args=[str(self.id)])

    class Meta:
        verbose_name = 'Thread'
        verbose_name_plural = 'Threads'
        ordering = ["-created_on"]

class Comment(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ["created_on"]
