from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    return render(request, 'merchstore/index.html', {
        'products': Product.objects.all()
    })

def item(request, id):
    return render(request, 'merchstore/item.html', {
        'product': Product.objects.get(id=id)
    })
