from django.contrib import admin
from .models import *


class CommissionAdmin(admin.ModelAdmin):
    model = Commission
    list_display = ('title', 'description', 'created_on', 'updated_on',)
    search_fields = ('name',)

class JobAdmin(admin.ModelAdmin):
    model = Job
    list_display = ('commission', 'created_on', 'updated_on',)
    list_filter = ('commission',)

admin.site.register(Commission, CommissionAdmin)
admin.site.register(Job, JobAdmin)
