from django.urls import path
from .views import articles_list, article_detail, article_create, article_update

urlpatterns = [
    path('articles/', articles_list, name='articles_list'),
    path('article/<int:pk>/', article_detail, name='article_detail'),
    path('article/add/', article_create, name='article_create'),
    path('article/<int:pk>/edit/', article_update, name='article_update'),
]

app_name = 'wiki'