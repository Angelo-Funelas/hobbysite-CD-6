from django.urls import path
from .views import index, item, add, edit, cart, transactions
from django.shortcuts import redirect

urlpatterns = [
    path("", lambda request: redirect("merchstore:index")),
    path("items/", index, name="index"),
    path("item/<int:id>/", item, name="item"),
    path("item/add/", add, name="add"),
    path("item/<int:id>/edit/", edit, name="edit"),
    path("item/cart/", cart, name="cart"),
    path("item/transactions/", transactions, name="transactions"),
]

app_name = "merchstore"
