from django.urls import path
from django.shortcuts import redirect
from .views import thread_list, detailed_thread, create_thread, update_thread

urlpatterns = [
    path("", lambda request: redirect("forum:thread_list")),
    path("threads/", thread_list, name="thread_list"),
    path("thread/<int:id>/", detailed_thread, name="detailed_thread"),
    path("thread/add/", create_thread, name="create_thread"),
    path("thread/<int:id>/edit/", update_thread, name="update_thread"),
]

app_name = "forum"
