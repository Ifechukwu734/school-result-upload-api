from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUser


class CustomUserCreationForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ("email",)

    def clean_password(self):
        return self.cleaned_data.get('password')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("email",)