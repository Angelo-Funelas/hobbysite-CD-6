from django.db import models
from django.urls import reverse
from user_management.models import Profile

class ArticleCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["name"] #orders the names in ascending alphabetical order
        verbose_name = "Article Category"
        verbose_name_plural = "Article Categories"

class Article(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(ArticleCategory, on_delete=models.SET_NULL, null=True, related_name="article_category")
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name="blog_articles")
    header_image = models.ImageField(upload_to='blog/article_headers/', blank=True, null=True)
    

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ["-created_on"] #orders in descending date order

    def get_absolute_url(self):
        return reverse('blog:article_detail', kwargs={"article_id": self.id})

class Comment(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name="blog_comments")
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="blog_comments")
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author
    
    class Meta:
        ordering = ['created_on'] #orders in ascending date order