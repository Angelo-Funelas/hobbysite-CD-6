from django.urls import path
from .views import commission, commission_details, commission_create, commission_update, job_application
from django.shortcuts import redirect

urlpatterns = [
    path("", lambda request: redirect("commissions:commission")),
    path('list/', commission, name="commission"),
    path('detail/<int:id>/', commission_details, name="commission_details"),
    path('add/', commission_create, name="commission_create"),
    path('<int:id>/edit/', commission_update, name="commission_update"),
    path('job/<int:job_id>/', job_application, name="job_application"),
]

app_name = "commissions"
