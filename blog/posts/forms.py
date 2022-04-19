from dataclasses import fields
from tkinter import Widget
from xml.etree.ElementTree import Comment
from django import forms
from .models import Post, Comments

class PostForm(forms.ModelForm):
    class Meta:
            model = Post
            fields = ('__all__')

class CommentsForm(forms.ModelForm):
    content = forms.CharField(required=True, widget=forms.Textarea(attrs={
        "rows":4
    }))
    class Meta:
        model = Comments
        fields = ('content',)