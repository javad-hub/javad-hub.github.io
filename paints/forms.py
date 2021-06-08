from django import forms
from django.forms import ModelForm
from .models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('name','comment')
        lables = {
        'paint':'Choose which paint do you want to comment:',
        'name':"Enter your name:",
    }