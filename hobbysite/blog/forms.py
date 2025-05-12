from django import forms
from .models import Article, Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['entry']

class UpdateArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ['created_on', 'author']

class NewArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'category', 'entry', 'header_image']