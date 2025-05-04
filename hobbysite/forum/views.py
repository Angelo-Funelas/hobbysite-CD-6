from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import ThreadCategory, Thread, Comment
from .forms import CommentForm, ThreadForm

@login_required
def thread_list(request):
    username = request.user.profile
    user_threads = Thread.objects.filter(author=username)
    other_threads = Thread.objects.exclude(author=username)
    
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
        'other_threads': grouped_threads,
        'username': username
    })

def detailed_thread(request, thread_num):
    chosen_thread = Thread.objects.get(id=thread_num)
    other_threads = Thread.objects.filter(category=chosen_thread.category).exclude(id=thread_num)[:4]
    comments = Comment.objects.filter(thread=chosen_thread)

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
        'comments': comments,
        'comment_form': comment_form
    })

@login_required
def create_thread(request):
    if request.method == "POST":
        thread_form = ThreadForm(request.POST)
        thread = thread_form.save(commit=False)
        thread.author = request.user.profile
        thread.save()
        return redirect('forum:detailed_thread', thread.id)
    
    thread_form = ThreadForm()

    return render(request, 'forum/create_thread.html', {
        'thread_form': thread_form
    })