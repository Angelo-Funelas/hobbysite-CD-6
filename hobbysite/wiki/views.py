from django.shortcuts import render
from .models import *

def articles_list(request):
    ctx = {
        "articles": Article.objects.all(),
        "categories": ArticleCategory.objects.all()
    }
    return render(request, "articles_list.html", ctx)

def article_detail(request, pk):
    ctx = {
        "article": Article.objects.get(pk=pk)
    }
    return render(request, "article.html", ctx)