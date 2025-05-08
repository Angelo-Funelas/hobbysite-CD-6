from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import ArticleCategory, Article, Comment
from .forms import CommentForm, NewArticleForm, UpdateArticleForm

def articles_list(request):
    return render(request, 'wiki/articles_list.html', {
        'user_articles': Article.objects.filter(author=request.user.profile),
        'all_articles': Article.objects.exclude(author=request.user.profile),
        'categories': ArticleCategory.objects.all()
    })

def article_detail(request, pk): # Unfinished, will work on specifications later
    return render(request, 'wiki/article.html', {
        'article': Article.objects.get(pk=pk)
    })

@login_required
def article_create(request):
    if request.method == 'POST':
        article_form = NewArticleForm(request.POST, request.FILES)
        if article_form.is_valid():
            article = article_form.save(commit=False)
            article.author = request.user.profile
            article.save()
            return redirect('article_detail', pk=article.pk)
    else:
        article_form = NewArticleForm()

    return render(request, 'wiki/create_article.html', {
        'article_form': article_form
    })

@login_required
def article_update(request, pk):
    article = Article.objects.get(pk=pk)
    if article.author != request.user.profile:
        return redirect('article_detail', pk=pk)
    
    if request.method == 'POST':
        article_form = UpdateArticleForm(request.POST, request.FILES, instance=article)
        if article_form.is_valid():
            article_form.save()
            return redirect('article_detail', pk=pk)
    else:
        article_form = UpdateArticleForm(instance=article)

    return render(request, 'wiki/update_article.html', {
        'article': article,
        'article_form': article_form
    })