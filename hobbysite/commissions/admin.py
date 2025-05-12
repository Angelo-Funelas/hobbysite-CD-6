from django.contrib import admin
from .models import Commission, Job, JobApplication
from django.contrib.auth.decorators import login_required



class CommissionAdmin(admin.ModelAdmin):
    model = Commission
    list_display = ('title', 'description', 'status', 'created_on', 'updated_on',)
    search_fields = ('name',)

class JobAdmin(admin.ModelAdmin):
    model = Job
    list_display = ('commission', 'status', 'created_on', 'updated_on',)
    list_filter = ('commission',)

class JobApplicationAdmin(admin.ModelAdmin):
    model = JobApplication
    list_display = ('job', 'applicant', 'status', 'applied_on',)
    list_filter = ('job',)
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.annotate(
            status_order=Case(
                When(status='pending', then=0),
                When(status='accepted', then=1),
                When(status='rejected', then=2),
                output_field=IntegerField(),
            )
        ).order_by('status_order', '-applied_on')

admin.site.register(Commission, CommissionAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(JobApplication, JobApplicationAdmin)
