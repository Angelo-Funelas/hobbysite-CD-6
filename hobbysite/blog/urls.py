from django.urls import path
from .views import *

urlpatterns = [
    path("articles", articles_list, name="index"),
    path("article/<int:article_id>", article_detail, name="item"),
]

app_name = "blog"