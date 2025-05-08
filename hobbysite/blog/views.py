from django.shortcuts import render
from .models import Article

def articles_list(request):
    return render(request, 'blog/article_list.html', {
        'articles': Article.objects.all()
    })

def article_detail(request, article_id):
    return render(request, 'blog/article_detail.html', {
        'article': Article.objects.get(id=article_id)
    })