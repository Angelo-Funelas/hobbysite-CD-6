from django.shortcuts import render
from .models import *

def thread_list(request):
    
    threads = 
    return render(request, 'thread_list.html', {'threads': threads})

def detailed_thread(request, thread_num):

    thread = 
    return render(request, 'thread.html', {'thread': thread})
