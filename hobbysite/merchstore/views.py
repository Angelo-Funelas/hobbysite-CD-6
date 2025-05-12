from django.shortcuts import render, redirect
from .models import Product, Transaction, ProductType, ProductImage
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect
from urllib.parse import urlencode, quote
from django.db.models import Sum

def index(request):
    user_profile = request.user.profile if request.user.is_authenticated else None
    
    if user_profile:
        user_products = Product.objects.filter(owner=user_profile)
        all_products = Product.objects.exclude(owner=user_profile)
    else:
        user_products = None
        all_products = Product.objects.all()
        
    return render(request, 'merchstore/index.html', {
        'user_products': user_products,
        'products': all_products
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
    product.sales = product.purchases.aggregate(Sum('amount'))['amount__sum']
    return render(request, 'merchstore/item.html', {
        'product': product
    })

def handle_images(product, files, count, to_delete):
    for i in range(1, count+1):
        image = files[f"image-{i}"]
        product_image = ProductImage(product=product, image=image)
        product_image.save()
    for id in to_delete.split():
        id = int(id)
        try:
            ProductImage.objects.get(pk=id).delete()
        except:
            pass
        
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
        handle_images(product, request.FILES, int(request.POST['image_count']), request.POST['images_to_delete'])
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
        handle_images(product, request.FILES, int(request.POST['image_count']), request.POST['images_to_delete'])
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
        if transaction.product.owner not in grouped_transactions:
            grouped_transactions[transaction.product.owner] = []
        transaction.total_price = transaction.amount * transaction.product.price
        grouped_transactions[transaction.product.owner].append(transaction)
    return render(request, 'merchstore/transactions.html', {
        "heading": "Your Cart",
        "grouped_transactions": grouped_transactions
    })

@login_required
def transactions(request):
    grouped_transactions = {}
    for transaction in Transaction.objects.filter(product__owner=request.user.profile):
        if transaction.buyer not in grouped_transactions:
            grouped_transactions[transaction.buyer] = []
        transaction.total_price = transaction.amount * transaction.product.price
        grouped_transactions[transaction.buyer].append(transaction)
    return render(request, 'merchstore/transactions.html', {
        "heading": "Your Sales",
        "grouped_transactions": grouped_transactions
    })