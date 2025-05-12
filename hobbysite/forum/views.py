from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import ThreadCategory, Thread, Comment
from .forms import CommentForm, ThreadForm

def thread_list(request):
    if request.user.is_authenticated:
        user_profile = request.user.profile
        user_threads = Thread.objects.filter(author=user_profile)
        threads = Thread.objects.exclude(author=user_profile)
    
    else:
        user_profile = None
        user_threads = None
        threads = Thread.objects.all()
    
    # Iterates through all categories and then groups them into respective dictionaries
    categories = ThreadCategory.objects.all()
    grouped_threads = []
    for category in categories:
        threads_in_category = threads.filter(category=category)
        if threads_in_category.exists():
            grouped_threads.append({
                'category': category,
                'threads': threads_in_category
            })

    return render(request, 'forum/thread_list.html', {
        'user_threads': user_threads,
        'all_threads': grouped_threads,
        'user_profile': user_profile,
        'categories': categories
    })

def detailed_thread(request, thread_num):
    chosen_thread = Thread.objects.get(id=thread_num)
    other_threads = Thread.objects.filter(category=chosen_thread.category).exclude(id=thread_num)[:4]
    comments = Comment.objects.filter(thread=chosen_thread)
    categories = ThreadCategory.objects.all()

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        new_comment = comment_form.save(commit=False)
        new_comment.author = request.user.profile
        new_comment.thread = chosen_thread
        new_comment.save()
        return redirect('forum:detailed_thread', thread_num)

    comment_form = CommentForm()

    return render(request, 'forum/thread.html', {
        'thread': chosen_thread,
        'other_threads': other_threads,
        'categories': categories,
        'comments': comments,
        'comment_form': comment_form
    })

@login_required
def create_thread(request):
    if request.method == "POST":
        thread_form = ThreadForm(request.POST, request.FILES)
        thread = thread_form.save(commit=False)
        thread.author = request.user.profile
        thread.save()
        return redirect('forum:detailed_thread', thread.id)
    
    thread_form = ThreadForm()

    return render(request, 'forum/create_thread.html', {
        'thread_form': thread_form
    })

@login_required
def update_thread(request, thread_num):
    chosen_thread = Thread.objects.get(id=thread_num)
    if request.method == "POST":
        update_form = ThreadForm(request.POST, request.FILES, instance=chosen_thread)
        update_form.save()
        return redirect('forum:detailed_thread', chosen_thread.id)
    
    update_form = ThreadForm(instance=chosen_thread)

    return render(request, 'forum/update_thread.html', {
        'thread': chosen_thread,
        'update_form': update_form
    })
    