from django.urls import path
from . import views
from django.shortcuts import redirect

urlpatterns = [
    path("", lambda request: redirect("merchstore:index")),
    path("items/", views.index, name="index"),
    path("item/<int:id>/", views.item, name="item"),
    path("item/add/", views.add, name="add"),
    path("item/<int:id>/edit/", views.edit, name="edit"),
    path("item/cart", views.cart, name="cart"),
    path("item/transactions", views.transactions, name="transactions"),
]

app_name = "merchstore"
