from django.shortcuts import render
from .models import *

def articles_list(request):
    return render(request, "article_list.html", 
                  {"articles": Article.objects.all()})

def article_detail(request, article_id):
    return render(request, "article_detail.html", {
        "article": Article.objects.get(id=article_id)
    })
# Create your views here.
