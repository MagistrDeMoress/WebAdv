from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.forms.fields import EmailField
from django.forms.forms import Form

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя:', min_length=5, max_length=35)
    email = forms.EmailField(label='Email:')
    password1 = forms.CharField(label='Пароль:', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Подтвердите пароль:', widget=forms.PasswordInput)
    
    def username_clean(self):
        username = self.cleaned_data['username'].lower()
        new = User.objects.filter(username=username)
        if new.count():
            raise ValidationError('Пользователь уже существует')
        return username
    
    def email_clean(self):
        email = self.cleaned_data['email'].lower()
        new = User.objects.filter(email=email)
        if new.count():
            raise ValidationError('Пользователь с таким адресом уже существует')
        return email
    
    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            raise ValidationError('Неверное подтверждение пароля')
        return password2
    
    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user