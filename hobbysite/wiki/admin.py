from django.contrib import admin
from .models import ArticleCategory, Article, Comment

class CommentInline(admin.StackedInline):
    model = Comment

class ArticleCategoryAdmin(admin.ModelAdmin):
    model = ArticleCategory
    list_display = ('name', 'description',)
    search_fields = ('name',)

class ArticleAdmin(admin.ModelAdmin):
    model = Article
    list_display = ('title', 'author', 'category', 'created_on', 'updated_on',)
    list_filter = ('category', 'author',)
    inlines = [CommentInline,]

class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_display = ('author', 'article', 'entry', 'created_on', 'updated_on',)

admin.site.register(ArticleCategory, ArticleCategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)