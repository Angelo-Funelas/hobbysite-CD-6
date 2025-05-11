from django import forms
from .models import *

class CreateCommissionForm(forms.ModelForm):
    class Meta:
        model = Commission
        fields = ['title', 'description', 'status']

class CreateJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = [ 'role', 'entry', 'manpower_required', 'status']

class UpdateJobForm(forms.ModelForm):
    role = forms.CharField(required=False)
    entry = forms.CharField(required=False)
    manpower_required = forms.IntegerField(min_value=0,required=False)
    status = forms.ChoiceField(choices=Job.STATUS_CHOICES, required=False)

    class Meta:
        model = Job
        fields = ['role', 'entry', 'manpower_required', 'status']

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = [] 
