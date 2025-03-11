from django.shortcuts import render
from .models import *

def article_list(request):
    articles = Article.objects.all()

# Create your views here.
