from django.urls import path
from . import views

urlpatterns = [
    path("articles", [], name="index"),
    path("article/<int:num>", [], name="item"),
]

app_name = "blog"