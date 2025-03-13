from django.shortcuts import render
from .models import *

# Create your views here.
def commission(request):
    return render(request, 'commissions/commissions.html', {
        "commissions": Commission.objects.all()
    })

def commission_details(request, pk):
    return render(request, 'commissions/commissions_detail.html', {
        "commission": Commission.objects.get(pk=pk),
        "comments": Commission.objects.get(pk=pk).comments.all()
    })

