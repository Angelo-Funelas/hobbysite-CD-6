from django.urls import path
from .views import *
from django.shortcuts import redirect

urlpatterns = [
    path("", lambda request: redirect("merchstore:index")),
    path("items", index, name="index"),
    path("item/<int:id>", item, name="item"),
]

app_name = "merchstore"