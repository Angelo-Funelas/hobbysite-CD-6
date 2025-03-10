from django.shortcuts import render
from .models import *

def thread_list(request):
    return render(request, 'thread_list.html', {
        'threads': PostCategory.objects.all()
    })

def threads_in_category(request, category_name):
    chosen_category = PostCategory.objects.get(name=category_name)
    return render(request, 'threads_in_category.html', {
        'threads': Post.objects.filter(category=chosen_category),
        'chosen_category': chosen_category
    })

def detailed_thread(request, thread_num):
    return render(request, 'thread.html', {
        'thread': Post.objects.get(id=thread_num)
    })
