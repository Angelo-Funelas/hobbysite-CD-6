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
        return render(request, 'merchstore/add_edit.html', {
            "product_types": ProductType.objects.all()
        })

@login_required
def edit(request, id):
    product = Product.objects.get(pk=id)
    if not request.user.profile == product.owner:
        return HttpResponseRedirect(reverse('merchstore:item', kwargs={'id': id}))
    if request.method == "POST":
        product.name = request.POST['name']
        product.product_type = ProductType.objects.get(pk=request.POST['type'])
        product.description = request.POST['description']
        product.price = request.POST['price']
        product.save()
        product.update_status()
        return HttpResponseRedirect(reverse('merchstore:item', kwargs={'id': id}))
    else:
        return render(request, 'merchstore/add_edit.html', {
            "product": Product.objects.get(pk=id),
            "product_types": ProductType.objects.all()
        })

@login_required
def cart(request):
    grouped_transactions = {}
    for transaction in Transaction.objects.filter(buyer=request.user.profile):
        if transaction.buyer not in grouped_transactions:
            grouped_transactions[transaction.buyer] = []
        grouped_transactions[transaction.buyer].append(transaction)
    return render(request, 'merchstore/product_list.html', {
        "heading": "Your Cart",
        "grouped_transactions": grouped_transactions
    })

@login_required
def transactions(request):
    grouped_transactions = {}
    for transaction in Transaction.objects.filter(product__owner=request.user.profile):
        if transaction.buyer not in grouped_transactions:
            grouped_transactions[transaction.buyer] = []
        grouped_transactions[transaction.buyer].append(transaction)
    return render(request, 'merchstore/product_list.html', {
        "heading": "Your Sales",
        "grouped_transactions": grouped_transactions
    })