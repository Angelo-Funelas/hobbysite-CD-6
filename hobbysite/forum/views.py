from django.shortcuts import render
from .models import *

def thread_list(request):
    '''
    This view generates the webpage that displays the list of all Post Categories.

    '''
    return render(request, 'forum/thread_list.html', {
        'threads': PostCategory.objects.all()
    })

def threads_in_category(request, category_name):
    '''
    This view generates the webpage that displays all the threads in the chosen Post Category.

    '''
    chosen_category = PostCategory.objects.get(name=category_name)
    return render(request, 'forum/threads_in_category.html', {
        'threads': Post.objects.filter(category=chosen_category),
        'chosen_category': chosen_category
    })

def detailed_thread(request, thread_num):
    '''
    This view generates the webpage that displays all the details in a specific thread/Post.

    '''
    return render(request, 'forum/thread.html', {
        'thread': Post.objects.get(id=thread_num)
    })
