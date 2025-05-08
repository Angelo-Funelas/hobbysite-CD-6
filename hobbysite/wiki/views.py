from django.shortcuts import render
from .models import ArticleCategory, Article

def articles_list(request):
    return render(request, 'wiki/articles_list.html', {
        'articles': Article.objects.all(),
        'categories': ArticleCategory.objects.all()
    })

def article_detail(request, pk):
    return render(request, 'wiki/article.html', {
        'article': Article.objects.get(pk=pk)
    })