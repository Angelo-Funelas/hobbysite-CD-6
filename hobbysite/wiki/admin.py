from django.contrib import admin
from .models import *

class ArticleCategoryAdmin(admin.ModelAdmin):
    model = ArticleCategory
    list_display = ('name', 'description',)
    search_fields = ('name',)

class ArticleAdmin(admin.ModelAdmin):
    model = Article
    list_display = ('title', 'category', 'created_on', 'updated_on',)
    list_filter = ('category',)

admin.site.register(ArticleCategory, ArticleCategoryAdmin)
admin.site.register(Article, ArticleAdmin)