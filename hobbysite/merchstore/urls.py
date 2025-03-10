from django.urls import path
from . import views
from django.shortcuts import redirect

urlpatterns = [
    path("", lambda request: redirect("index")),
    path("items", views.index, name="index"),
    path("item/<int:itemID>", views.item, name="item"),
]

app_name = "merchstore"