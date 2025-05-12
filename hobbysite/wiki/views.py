from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import ArticleCategory, Article, Comment
from .forms import CommentForm, NewArticleForm, UpdateArticleForm

def articles_list(request):
    user_profile = request.user.profile if request.user.is_authenticated else None

    if user_profile:
        user_articles = Article.objects.filter(author=user_profile)
        all_articles = Article.objects.exclude(author=user_profile)
    else:
        user_articles = None
        all_articles = Article.objects.all()

    categories = ArticleCategory.objects.all()
    category_articles = {
        category: all_articles.filter(category=category) for category in categories
    }

    return render(request, 'wiki/articles_list.html', {
        'user_articles': user_articles,
        'category_articles': category_articles
    })

def article_detail(request, id): 
    article = Article.objects.get(id=id)
    related_articles = Article.objects.filter(category=article.category).exclude(id=id)[:2]
    comments = article.comment_set.all().order_by('-created_on')
    
    if request.method == "POST" and request.user.is_authenticated:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.author = request.user.profile
            comment.save()
            return redirect(article.get_absolute_url())
    else:
        comment_form = CommentForm()
    
    return render(request, 'wiki/article.html', {
        'article': article,
        'related_articles' : related_articles,
        'comments' : comments,
        'comment_form': comment_form
    })

@login_required
def article_create(request):
    if request.method == 'POST':
        article_form = NewArticleForm(request.POST, request.FILES)
        if article_form.is_valid():
            article = article_form.save(commit=False)
            article.author = request.user.profile
            article.save()
            return redirect(article.get_absolute_url())
    else:
        article_form = NewArticleForm()

    return render(request, 'wiki/create_article.html', {
        'article_form': article_form
    })

@login_required
def article_update(request, id):
    article = Article.objects.get(id=id)
    if article.author != request.user.profile:
        return redirect(article.get_absolute_url())
    
    if request.method == 'POST':
        article_form = UpdateArticleForm(request.POST, request.FILES, instance=article)
        if article_form.is_valid():
            article_form.save()
            return redirect(article.get_absolute_url())
    else:
        article_form = UpdateArticleForm(instance=article)

    return render(request, 'wiki/update_article.html', {
        'article': article,
        'article_form': article_form
    })