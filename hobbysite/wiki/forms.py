from django import forms
from .models import Article, Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['entry']


class NewArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'category', 'header_image']

class UpdateArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'category', 'header_image']