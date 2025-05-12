from django import forms
from .models import Thread, ThreadCategory, Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['entry']
        widgets = {
            'entry': forms.Textarea(attrs={
                'placeholder': 'Share your thoughts'
            })
        }
        labels = {
            'entry': ''
        }

class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['title', 'category', 'entry', 'image']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Input Title'
            }),
            'entry': forms.Textarea(attrs={
                'placeholder': 'Write your post...'
            }),
            'image': forms.FileInput()
        }
        labels = {
            'title': '',
            'entry': '',
            'category': 'Select Thread Category',
            'image': 'Upload an Image (Optional)'
        }
