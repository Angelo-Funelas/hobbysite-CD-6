from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect

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
    if request.method == "POST":
        name = request.POST['name']
        product_type = ProductType.objects.get(pk=request.POST['type'])
        stock = request.POST['stock']
        owner = request.user.profile
        description = request.POST['description']
        price = request.POST['price']
        product = Product(name=name, product_type=product_type, stock=stock, owner=owner, description=description, price=price)
        product.save()
        return HttpResponseRedirect(reverse('merchstore:item', kwargs={'id': product.id}))
    else:
        return render(request, 'merchstore/add.html', {
            "product_types": ProductType.objects.all()
        })

def edit(request):
    return

def cart(request):
    return

def transactions(request):
    return