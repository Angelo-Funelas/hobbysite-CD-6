from django.urls import path
from .views import *

urlpatterns = [
    path('/forum/threads', thread_list, name="thread_list"),
    path('/forum/thread/<int:thread_num', detailed_thread, name="detailed_thread"),
]

app_name = "forum"
