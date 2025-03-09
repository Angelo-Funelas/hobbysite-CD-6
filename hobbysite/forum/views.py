from django.shortcuts import render
from .models import *

def thread_list(request):
    
    threads = PostCategory.objects.all()
    return render(request, 'thread_list.html', {'threads': threads})

def threads_in_category(request, category_name):

    threads = PostCategory.objects.get(name=category_name)
    return render(request, 'threads_in_category.html', {'threads': threads})

def detailed_thread(request, thread_num):

    thread = Post.objects.get(id=thread_num)
    return render(request, 'thread.html', {'thread': thread})
