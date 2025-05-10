from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Article, Comment
from user_management.models import Profile
from .forms import CommentForm

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
    try:
        article = Article.objects.select_related('author').get(id=article_id)
    except Article.DoesNotExist:
        article = None
    
    comments = []
    related_articles = []
    form = None

    if article:
        comments = article.comments.select_related('author').all().order_by('-created_on')
        related_articles = Article.objects.filter(author=article.author).exclude(id=article.id)[:2]

        if request.user.is_authenticated:
            try:
                user_profile = request.user.profile
            except Profile.DoesNotExist:
                user_profile = None
            
            if request.method == "POST":
                form = CommentForm(request.POST)
                if form.is_valid():
                    comment = form.save(commit=False)
                    comment.author = user_profile
                    comment.article = article
                    comment.save()
                    return redirect("blog:item", article_id=article.id)
            else:
                form = CommentForm()
    
    return render(request, "blog/article_detail.html", {
        "article": article,
        "comments": comments,
        "related_articles": related_articles,
        "form": form,
    })
