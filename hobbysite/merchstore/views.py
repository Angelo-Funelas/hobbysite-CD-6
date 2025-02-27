from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    return render(request, "index.html", {
        "products": Product.objects.all()
    })

def item(request, itemID):
    return render(request, "item.html")