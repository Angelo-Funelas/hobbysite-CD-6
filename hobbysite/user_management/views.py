from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse

@login_required
def index(request):
    if request.method == 'POST':
        display_name = request.POST['display-name']
        email = request.POST['email']
        profile = request.user.profile
        profile.display_name = display_name
        profile.email_field = email
        profile.save()
    else:
        return render(request, "user_management/profile.html", {
            "profile": request.user.profile
        })
        
def register(request):
    if request.method == 'GET':
        return render(request, "registration/register.html")
    elif request.method == 'POST':
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        try: 
            User.objects.get(username=username.lower())
        except User.DoesNotExist:
            try:
                pfp = request.FILES["pfp"]
                User.objects.create_user(username.lower(), email, password, pfp=pfp, display_name=username)
            except:
                user = User.objects.create_user(username.lower(), email, password, display_name=username) 
            return HttpResponseRedirect(reverse('index'))