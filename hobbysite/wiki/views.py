from django.shortcuts import render
from .models import *

# Create your views here.
def articles_list(request):
    return render(request, "articles_list.html", {"articles": Article.objects.all()})

def article_detail(request, pk):
    return render(request, "article.html", {"article": Article.objects.get(pk=pk)})