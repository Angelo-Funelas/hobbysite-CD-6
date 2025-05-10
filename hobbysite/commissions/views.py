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
        applied_commissions = Commission.objects.filter(
        jobs__job_application__applicant=user_profile
        ).annotate(status_order=custom_order).distinct().order_by('status_order', 'created_on')
        other_commissions = Commission.objects.exclude(author=user_profile).annotate(
            status_order=custom_order
        ).order_by('status_order', 'created_on')

    else:
        user_commissions = Commission.objects.none()
        applied_commissions = Commission.objects.none()
        other_commissions = Commission.objects.all()

    return render(request, 'commissions/commissions.html', {
        'user_commissions': user_commissions,
        'applied_commissions': applied_commissions,
        'other_commissions': other_commissions,
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
        if commission_form.is_valid():
            commission = commission_form.save(commit=False)
            commission.author = request.user.profile
            commission.save()
            
            return redirect('commissions:commission_details', pk=commission.pk)
        
    commission_form = CreateCommissionForm()

    return render(request, 'commissions/commissions_add.html', {
        'commission_form': commission_form,
        })



def commission_update(request, pk):
    commission_object = Commission.objects.get(pk=pk)
    jobs = Job.objects.filter(commission=commission_object)

    if commission_object.author != request.user.profile:
        return redirect('commission:commissions_detail', pk=pk)

    if request.method == 'POST':
        commission_form = CreateCommissionForm(request.POST, request.FILES, instance=commission_object)
        job_forms = [
            CreateJobForm(request.POST, request.FILES, prefix=str(job.id), instance=job) for job in jobs
        ]
        new_job_form = UpdateJobForm(request.POST, request.FILES)

        if commission_form.is_valid() and all([jf.is_valid() for jf in job_forms]) and new_job_form.is_valid():
            commission = commission_form.save(commit=False)
            commission_form.save()
            if all(new_job_form.cleaned_data.get(field) for field in new_job_form.cleaned_data):
                job = new_job_form.save(commit=False)
                job.author = request.user.profile
                job.commission = commission
                job.save()
            for job_form in job_forms:
                job_form.save()
                return redirect('commissions:commission_details', pk=pk)
                
    else:
        commission_form = CreateCommissionForm(instance=commission_object)
        job_forms = [
            CreateJobForm(prefix=str(job.id), instance=job) for job in jobs
        ]
        new_job_form = UpdateJobForm()
    
    return render(request, 'commissions/commissions_update.html', {
        'commission_form': commission_form,
        'job_forms': job_forms,
        'new_job_form': new_job_form,
    })
    
