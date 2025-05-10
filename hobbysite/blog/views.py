from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Article, ArticleCategory, Comment
from user_management.models import Profile

def articles_list(request):
    category_grouping = {}
    user_articles = []

    articles = Article.objects.select_related('category', 'author').all()

    if request.user.is_authenticated:
        try:    
            user_profile = request.user.profile
            user_articles = articles.filter(author=user_profile)
            articles = articles.exclude(author=user_profile)
        except Profile.DoesNotExist:
            pass

    for article in articles:
        if article.category:
            category_name = article.category.name
        else:
            category_name = "Uncategorized"
        if category_name not in category_grouping:
            category_grouping[category_name] = []
        category_grouping[category_name].append(article)
    
    context = {
        "user_articles": user_articles,
        "category_grouping": category_grouping,
    }

    return render(request, 'blog/article_list.html', context)

def article_detail(request, article_id):
    return render(request, 'blog/article_detail.html', {
        'article': Article.objects.get(id=article_id)
    })