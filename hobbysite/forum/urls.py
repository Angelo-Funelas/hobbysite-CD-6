from django.urls import path
from .views import *

urlpatterns = [
    path('threads', thread_list, name="thread_list"),
    path('threads/<str:category_name>', threads_in_category, name="threads_in_category"),
    path('thread/<int:thread_num>', detailed_thread, name="detailed_thread"),
]

app_name = "forum"
