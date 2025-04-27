from django.urls import path
from .views import index, register
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", index, name="index"),
    path("register/", register, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="user_management/login.html"), name="login"),
    path("login/", auth_views.LogoutView.as_view(), name="logout"),
    path("password_reset/", auth_views.PasswordResetView.as_view(template_name="user_management/password_reset_form.html"), name="password_reset"),
    path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(template_name="user_management/password_reset_done.html"), name="password_reset_done"),
    path("password_reset/confirm/", auth_views.PasswordResetConfirmView.as_view(template_name="user_management/password_reset_confirm.html"), name="password_reset_confirm"),
    path("password_reset/complete/", auth_views.PasswordResetCompleteView.as_view(template_name="user_management/password_reset_complete.html"), name="password_reset_complete"),
]
