from django.contrib import admin
from .models import *

class PostCategoryAdmin(admin.ModelAdmin):
    model = PostCategory

    list_display = ('name', 'description',)
    search_fields = ('name', )

class PostAdmin(admin.ModelAdmin):
    model = Post

    list_display = ('title', 'category', 'entry', 'created_on', 'updated_on',)
    search_fields = ('title', 'entry',)
    list_filter = ('created_on',)

admin.site.register(PostCategory, PostCategoryAdmin)
admin.site.register(Post, PostAdmin)
