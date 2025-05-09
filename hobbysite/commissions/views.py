from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *


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

@login_required
def commission_create(request):
    if request.method == "POST":
        commission_form = CreateCommissionForm(request.POST, request.FILES)
        job_form = CreateJobForm(request.POST, request.FILES)
        if commission_form.is_valid() and job_form.is_valid():
            commission = commission_form.save(commit=False)
            commission.author = request.user.profile
            commission.save()
            job = job_form.save(commit=False)
            job.author = request.user.profile
            job.commission = commission
            job.save()
            
            return redirect('commissions:commission_details', pk=commission.pk)
        
    commission_form = CreateCommissionForm()
    job_form = CreateJobForm()

    return render(request, 'commissions/commissions_add.html', {
        'commission_form': commission_form,
        'job_form': job_form,
        })



#def commission_update(request, pk):

#def job(request):

#TODO
#Make a commission lists view
#Make a commission detail view
#Make a commission create view
#Make a commission update view
#Make a job view
