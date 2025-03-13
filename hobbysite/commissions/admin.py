from django.contrib import admin
from .models import *

# Register your models here.

class CommissionAdmin(admin.ModelAdmin):
    model = Commission
    list_display = ['title', 'description', 'people_required', 'created_on', 'updated_on']
    search_fields = ['name']

class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_display = ['commission', 'created_on', 'updated_on']
    list_filter = ['commission']

admin.site.register(Commission, CommissionAdmin)
admin.site.register(Comment, CommentAdmin)
