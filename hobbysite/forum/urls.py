from django.urls import path
from .views import thread_list, detailed_thread

urlpatterns = [
    path("threads", thread_list, name="thread_list"),
    path("thread/<int:thread_num>", detailed_thread, name="detailed_thread"),
]

app_name = "forum"
