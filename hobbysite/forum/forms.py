from django import forms
from .models import Thread, ThreadCategory, Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['entry']

class NewThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['title', 'category', 'entry', 'image']

class UpdateThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        exclude = ['created_on', 'author']
