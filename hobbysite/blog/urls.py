from django.urls import path
from .views import article_list, article_detail, article_create, article_update
from django.shortcuts import redirect

urlpatterns = [
    path("", lambda request: redirect("blog:index")),
    path("articles/", article_list, name="index"),
    path("article/<int:article_id>/", article_detail, name="article_detail"),
    path('article/add/', article_create, name='article_create'),
    path('article/<int:article_id>/edit/', article_update, name='article_update'),
]

app_name = "blog"