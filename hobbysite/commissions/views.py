from django.shortcuts import render
from .models import *

# Create your views here.
def commission(request):
    return render(request, "commissions.html", {
        "commissions": Commission.objects.all()
    })

def commission_details(request, pk):
    return render(request, "commission_details.html", {
        "comments": Commission.objects.get(pk=pk)
    })

