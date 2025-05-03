from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import ThreadCategory, Thread

@login_required
def thread_list(request):
    user_threads = Thread.objects.filter(author=request.user.profile)
    other_threads = Thread.objects.exclude(author=request.user.profile)
    
    # Iterates through all categories and then groups them into respective dictionaries
    categories = ThreadCategory.objects.all()
    grouped_threads = []
    for category in categories:
        threads_in_category = other_threads.filter(category=category)
        if threads_in_category.exists():
            grouped_threads.append({
                'category': category,
                'threads': threads_in_category
            })

    return render(request, 'forum/thread_list.html', {
        'user_threads': user_threads,
        'other_threads': grouped_threads
    })

# def threads_in_category(request, category_name):
#     chosen_category = ThreadCategory.objects.get(name=category_name)
#     return render(request, 'forum/threads_in_category.html', {
#         'threads': Thread.objects.filter(category=chosen_category),
#         'chosen_category': chosen_category
#     })

def detailed_thread(request, thread_num):
    return render(request, 'forum/thread.html', {
        'thread': Thread.objects.get(id=thread_num)
    })
