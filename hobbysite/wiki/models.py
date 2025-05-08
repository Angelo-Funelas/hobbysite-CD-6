from django.db import models
from django.urls import reverse
from user_management.models import Profile

class ArticleCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name'] # Sorted by name in ascending order
        verbose_name = "Article category"
        verbose_name_plural = "Article categories"

class Article(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(ArticleCategory, on_delete=models.SET_NULL, null=True, related_name="articles")
    entry = models.TextField()
    header_image = models.ImageField(upload_to='images/', blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_on'] # Sorted by creation date in descending order

    def get_absolute_url(self):
        return reverse('wiki:article_detail', args=[self.pk])
    
class Comment(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_on']  # Sort by creation date in ascending order