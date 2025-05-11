from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'merchstore/index.html', {
        'user_products': Product.objects.filter(owner=request.user.profile) if request.user.is_authenticated else None,
        'products': Product.objects.exclude(owner=request.user.profile) if request.user.is_authenticated else Product.objects.all()
    })

def item(request, id):
    return render(request, 'merchstore/item.html', {
        'product': Product.objects.get(id=id)
    })

@login_required
def add(request):
    return

def edit(request):
    return

def cart(request):
    return

def transactions(request):
    return