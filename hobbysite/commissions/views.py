from django.shortcuts import render
from .models import *


def commission(request):
    return render(request, 'commissions/commissions.html', {
        'commissions': Commission.objects.all()
    })

def commission_details(request, pk):
    commission_object = Commission.objects.get(pk=pk)
    return render(request, 'commissions/commissions_detail.html', {
        'commission': commission_object,
        'jobs': commission_object.jobs.all()
    })

#TODO
#Make a commission lists view
#Make a commission detail view
#Make a commission create view
#Make a commission update view
#Make a job view
