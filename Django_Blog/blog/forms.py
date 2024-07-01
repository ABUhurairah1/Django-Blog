from django import forms
from .models import Blog,Comment


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['name','image','description']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']