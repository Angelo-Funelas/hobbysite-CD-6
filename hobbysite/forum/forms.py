from django import forms
from .models import Thread, ThreadCategory, Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['entry']
