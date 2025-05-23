from django.contrib import admin
from .models import Article, ArticleCategory

class ArticleCategoryAdmin(admin.ModelAdmin):
    model = ArticleCategory
    list_display = ('name',)
    search_fields = ('name',)

class ArticleAdmin(admin.ModelAdmin):
    model = Article
    list_display = ('title', 'author', 'category', 'created_on', 'updated_on',)
    list_filter = ('category', 'created_on',)
    search_fields = ('title', 'content',)

admin.site.register(ArticleCategory, ArticleCategoryAdmin)
admin.site.register(Article, ArticleAdmin)