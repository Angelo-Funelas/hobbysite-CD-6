from django.urls import path
from .views import *

urlpatterns = [
    path('articles/', articles_list, name="articles_list"),
    path("recipe/<int:pk>/", article_detail, name="article_detail"),
]

app_name = "wiki"