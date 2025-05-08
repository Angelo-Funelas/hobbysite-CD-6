from django.urls import path
from .views import articles_list, article_detail
from django.shortcuts import redirect

urlpatterns = [
    path("", lambda request: redirect("blog:index")),
    path("articles", articles_list, name="index"),
    path("article/<int:article_id>", article_detail, name="item"),
]

app_name = "blog"