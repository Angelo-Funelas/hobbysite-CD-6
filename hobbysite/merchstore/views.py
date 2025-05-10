from django.shortcuts import render
from .models import *

def index(request):
    return render(request, 'merchstore/index.html', {
        'user_products': Product.objects.filter(owner=request.user.profile) if request.user.is_authenticated else None,
        'products': Product.objects.exclude(owner=request.user.profile) if request.user.is_authenticated else Product.objects.all()
    })

def item(request, id):
    return render(request, 'merchstore/item.html', {
        'product': Product.objects.get(id=id)
    })
