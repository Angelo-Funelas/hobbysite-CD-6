from django.urls import path
from . import views
from django.shortcuts import redirect

urlpatterns = [
    path("", lambda request: redirect("commission"))
    path('commissions/list', views.commission, name = "commission"),
    path('commissions/detail/<int:pk>/', views.commission_details, name = "commission_details"),
]

app_name = "commissions"