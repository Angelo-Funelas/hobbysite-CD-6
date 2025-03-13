from django.db import models
from django.urls import reverse

class PostCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('forum:threads_in_category', args=[self.name])

    # This function gets the latest created within the category by accessing the foreign key connected to the Post model.
    def latest_post(self):
        return self.posts.order_by('-created_on')[0]

    class Meta:
        verbose_name = 'Post Category'
        verbose_name_plural = 'Post Categories'
        ordering = ["name"]

class Post(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(PostCategory, on_delete=models.SET_NULL, null=True, related_name="posts")
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('forum:detailed_thread', args=[str(self.id)])
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ["-created_on"]
