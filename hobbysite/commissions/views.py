from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.db.models import Case, When, Value, IntegerField
from .forms import *


def commission(request):
    user_profile = request.user.profile if request.user.is_authenticated else None
    custom_order = Case(
        When(status='open', then=Value(0)),
        When(status='full', then=Value(1)),
        When(status='completed', then=Value(2)),
        When(status='discontinued', then=Value(3)),
        output_field=IntegerField()
    )

    if user_profile:
        user_commissions = Commission.objects.filter(author=user_profile).annotate(
            status_order=custom_order
        ).order_by('status_order', 'created_on')
        other_commissions = Commission.objects.exclude(author = request.user.profile).annotate(
            status_order=custom_order
        ).order_by('status_order', 'created_on')

    else:
        user_commissions = Commission.objects.none()
        other_commissions = Commission.objects.all()

    return render(request, 'commissions/commissions.html', {
        'user_commissions': user_commissions,
        'other_commissions': other_commissions
    })

def commission_details(request, pk):
    commission_object = Commission.objects.get(pk=pk)
    jobs = commission_object.jobs.all()
    return render(request, 'commissions/commissions_detail.html', {
        'commission': commission_object,
        'jobs': jobs
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
