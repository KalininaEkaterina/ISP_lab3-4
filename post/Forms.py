from .models import Nursery
from django.forms import ModelForm, TextInput, Textarea
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class TaskForm(ModelForm):
    class Meta:
        model = Nursery
        fields = ["name", "descr"]
        widgets = {
            "name":TextInput(attrs={
               'class': 'form-control',
               'placeholder': 'Введите название'
        }),
            "descr": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
        }),
        }


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']