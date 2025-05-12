from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Article, Comment, ArticleCategory
from user_management.models import Profile
from .forms import CommentForm, NewArticleForm, UpdateArticleForm

def article_list(request):
    user_profile = request.user.profile if request.user.is_authenticated else None

    if user_profile:
        user_articles = Article.objects.filter(author=user_profile).order_by('created_on')
        other_articles = Article.objects.exclude(author=user_profile).order_by('-created_on')
    else:
        user_articles = None
        other_articles = Article.objects.all().order_by('-created_on')

    categories = ArticleCategory.objects.all().order_by('name')
    grouped_articles = {
        category: other_articles.filter(category=category)
        for category in categories
        if other_articles.filter(category=category).exists()
    }

    return render(request, 'blog/article_list.html', {
        'user_articles': user_articles,
        'grouped_articles': grouped_articles
    })

def article_detail(request, article_id):
    article = Article.objects.get(id=article_id)
    other_articles = Article.objects.filter(author=article.author).exclude(id=article_id)[:4]
    comments = Comment.objects.filter(article=article).order_by('created_on')

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.author = request.user.profile
            new_comment.article = article
            new_comment.save()
            return redirect(article.get_absolute_url)
    
    comment_form = CommentForm()

    return render(request, 'blog/article_detail.html', {
        'article': article,
        'other_articles': other_articles,
        'comments': comments,
        'comment_form': comment_form
    })

@login_required
def article_create(request):
    if request.method == 'POST':
        article_form = NewArticleForm(request.POST, request.FILES)
        if article_form.is_valid():
            new_article = article_form.save(commit=False)
            new_article.author = request.user.profile
            new_article.save()
            return redirect('blog:article_detail', article_id=new_article.id)
    
    article_form = NewArticleForm()

    return render(request, 'blog/article_create.html', {
        'article_form': article_form
    })

@login_required
def article_update(request, article_id):
    article = Article.objects.get(id=article_id)
    if article.author != request.user.profile:
        return redirect('blog:article_detail', article_id=article.id)
    
    if request.method == 'POST':
        update_form = UpdateArticleForm(request.POST, request.FILES, instance=article)
        if update_form.is_valid():
            update_form.save()
            return redirect('blog:article_detail', article_id=article.id)
        
    update_form = UpdateArticleForm(instance=article)

    return render(request, 'blog/article_update.html', {
        'article': article,
        'update_form': update_form
    })