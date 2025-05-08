from django import forms
from .models import *

class CreateCommissionForm(forms.ModelForm):
    class Meta:
        model = Commission
        fields = ['title', 'description', 'status']

class UpdateCommissionForm(forms.ModelForm):
    class Meta:
        model = Commission
        fields = ['title', 'description', 'status']

class CreateJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['entry', 'role', 'manpower_required', 'status']

class UpdateJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['entry', 'role', 'manpower_required', 'status']

#class JobApplicationForm(forms.ModelForm):
