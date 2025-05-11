from django.shortcuts import render, redirect
from .models import Product, Transaction, ProductType
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect
from urllib.parse import urlencode, quote

def index(request):
    return render(request, 'merchstore/index.html', {
        'user_products': Product.objects.filter(owner=request.user.profile) if request.user.is_authenticated else None,
        'products': Product.objects.exclude(owner=request.user.profile) if request.user.is_authenticated else Product.objects.all()
    })

def item(request, id):
    product = Product.objects.get(pk=id)
    if request.method == "POST":
        qty = int(request.POST["qty"])
        status = request.POST["status"]
        if not request.user.is_authenticated:
            next_url = product.get_absolute_url()
            params = urlencode({
                'qty': qty,
                'status': request.POST["status"],
            })
            next = f"{next_url}?{params}"
            return redirect(f"{reverse('login')}?next={quote(next)}")
        try:        
            product.purchase(request.user.profile, qty, status)
            transaction = Transaction(buyer=request.user.profile, product=product, amount=qty, status=status)
            transaction.save()
            return HttpResponseRedirect(reverse('merchstore:cart'))
        except ValueError:
            return redirect(product.get_absolute_url())
        
    qty = request.GET.get('qty')
    status = request.GET.get('status')
    if qty and status and request.user.is_authenticated:
        qty = int(qty)
        try:        
            product.purchase(request.user.profile, qty, status)
            transaction = Transaction(buyer=request.user.profile, product=product, amount=qty, status=status)
            transaction.save()
            return HttpResponseRedirect(reverse('merchstore:cart'))
        except ValueError:
            return redirect(product.get_absolute_url())

    return render(request, 'merchstore/item.html', {
        'product': product
    })

@login_required
def add(request):
    if request.method == "POST":
        name = request.POST['name']
        product_type = ProductType.objects.get(pk=request.POST['type'])
        stock = int(request.POST['stock'])
        owner = request.user.profile
        description = request.POST['description']
        price = request.POST['price']
        product = Product(name=name, product_type=product_type, stock=stock, owner=owner, description=description, price=price)
        product.save()
        product.update_status()
        return redirect(product.get_absolute_url())
    else:
        return render(request, 'merchstore/add_edit.html', {
            "product_types": ProductType.objects.all()
        })

@login_required
def edit(request, id):
    product = Product.objects.get(pk=id)
    if not request.user.profile == product.owner:
        return redirect(product.get_absolute_url())
    if request.method == "POST":
        product.name = request.POST['name']
        product.stock = int(request.POST['stock'])
        product.product_type = ProductType.objects.get(pk=request.POST['type'])
        product.description = request.POST['description']
        product.price = request.POST['price']
        product.save()
        product.update_status()
        return redirect(product.get_absolute_url())
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