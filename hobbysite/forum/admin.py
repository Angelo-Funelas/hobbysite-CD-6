from django.contrib import admin
from .models import Thread, ThreadCategory, Comment

class ThreadInLine(admin.StackedInline):
    model = Thread

class CommentInLine(admin.StackedInline):
    model = Comment

class ThreadCategoryAdmin(admin.ModelAdmin):
    model = ThreadCategory

    list_display = ('name', 'description',)
    search_fields = ('name',)

    # Allows for admin to view Threads under a ThreadCategory.
    inlines = (ThreadInLine, )

class ThreadAdmin(admin.ModelAdmin):
    model = Thread

    list_display = ('title', 'author', 'category', 'created_on', 'updated_on', 'id',)
    search_fields = ('title', 'entry',)
    list_filter = ('created_on',)

    # Allows for admin to view Comments under a Thread.
    inlines = (CommentInLine, )

class CommentAdmin(admin.ModelAdmin):
    model = Comment

    list_display = ('author', 'thread', 'entry', 'created_on',)

admin.site.register(ThreadCategory, ThreadCategoryAdmin)
admin.site.register(Thread, ThreadAdmin)
admin.site.register(Comment, CommentAdmin)
