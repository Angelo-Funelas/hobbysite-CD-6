from django.urls import path
from .views import *
from django.shortcuts import redirect

urlpatterns = [
    path("", lambda request: redirect("commissions:commission")),
    path('list/', commission, name="commission"),
    path('detail/<int:pk>/', commission_details, name="commission_details"),

]

app_name = "commissions"
