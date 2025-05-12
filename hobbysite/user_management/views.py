from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Profile
from merchstore.models import Transaction
from commissions.models import Commission
from django.contrib import messages

@login_required
def index(request):
    if request.method == 'POST':
        display_name = request.POST['display-name']
        email = request.POST['email']
        profile = request.user.profile
        profile.display_name = display_name
        profile.email_field = email
        try:
            profile.profile_picture = request.FILES["profile-picture"]
        except:
            pass
        profile.save()
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, "user_management/profile.html", {
            "purchases": Transaction.objects.filter(buyer=request.user.profile).order_by('-created_on'),
            "sales": Transaction.objects.filter(product__owner=request.user.profile).order_by('-created_on'),
            "wiki_articles": request.user.profile.wiki_articles.all().order_by('-created_on'),
            "blog_articles": request.user.profile.blog_articles.all().order_by('-created_on'),
            "threads": request.user.profile.threads.all().order_by('-created_on'),
            "commissions_created": Commission.objects.filter(author=request.user.profile).order_by('-created_on'),
            "commissions_joined": Commission.objects.filter(jobs__job_application__applicant=request.user.profile).order_by('-created_on'),
        })
        
def register(request):
    if request.method == 'GET':
        return render(request, "user_management/register.html")
    elif request.method == 'POST':
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["passwordConfirm"]
        
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return HttpResponseRedirect(reverse('register'))

        # Check if username already exists
        if User.objects.filter(username=username.lower()).exists():
            messages.error(request, "Username already taken.")
            return HttpResponseRedirect(reverse('register'))

        # Check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already in use.")
            return HttpResponseRedirect(reverse('register'))
        
        user = User.objects.create_user(username.lower(), email, password)
        profile = Profile.objects.create(
            user=user,
            display_name=username,
            email_address=email,
        )
        try:
            profile.profile_picture = request.FILES["profile-picture"]
            profile.save()
        except:
            pass
        return HttpResponseRedirect(reverse('login'))