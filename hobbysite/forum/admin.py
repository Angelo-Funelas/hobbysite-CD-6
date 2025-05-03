from django.contrib import admin
from .models import Thread, ThreadCategory

class ThreadInLine(admin.StackedInline):
    model = Thread

class ThreadCategoryAdmin(admin.ModelAdmin):
    model = ThreadCategory

    list_display = ('name', 'description',)
    search_fields = ('name', )

    # Allows for admin to view Threads under a ThreadCategory.
    inlines = [ThreadInLine, ]

class ThreadAdmin(admin.ModelAdmin):
    model = Thread

    list_display = ('title', 'category', 'entry', 'created_on', 'updated_on', 'id', )
    search_fields = ('title', 'entry',)
    list_filter = ('created_on',)

admin.site.register(ThreadCategory, ThreadCategoryAdmin)
admin.site.register(Thread, ThreadAdmin)
