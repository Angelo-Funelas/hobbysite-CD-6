from django.shortcuts import render
from .models import *

# Create your views here.
def commission(request):
    return render(request, 'commissions/commissions.html', {
        'commissions': Commission.objects.all()
    })

def commission_details(request, pk):
    commission_object = Commission.objects.get(pk=pk)
    return render(request, 'commissions/commissions_detail.html', {
        'commission': commission_object,
        'comments': commission_object.comments.all()
    })

