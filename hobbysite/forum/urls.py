from django.urls import path
from .views import thread_list, detailed_thread, create_thread

urlpatterns = [
    path("threads", thread_list, name="thread_list"),
    path("thread/<int:thread_num>", detailed_thread, name="detailed_thread"),
    path("thread/add", create_thread, name="create_thread"),
]

app_name = "forum"
