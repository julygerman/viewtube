from django.contrib.auth.forms import UserCreationForm
from .models import Comment
from django import forms
from django.forms import ModelForm
from django.contrib.auth import get_user_model
User = get_user_model()


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=100, help_text='Required*')
    username = forms.CharField(max_length=100, help_text='Required*')
    name = forms.CharField(max_length=100, required=True, help_text='Required*')
    avatar = forms.CharField(max_length=300, required=False, help_text='Optional')    
    bio = forms.CharField(max_length=500, required=False, help_text='Optional')


    class Meta:
        model = User
        fields = ['username', 'name', 'email', 'avatar']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'date']
        widgets = {'date': forms.HiddenInput()}
        