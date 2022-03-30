from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Login'}),
                               label='')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
                               label='')


class CreateUserForm(forms.ModelForm):

    pass1 = forms.CharField(widget=forms.PasswordInput())
    pass2 = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        data = super().clean()
        if data['pass1'] != data['pass2']:
            raise ValidationError("Passwords don't match")

    class Meta:
        model = User
        fields = ['username']


class UserPermUpdateForm(forms.ModelForm):
    model = User
    fields = ['user_permissions']
    widgets = {
        'user_permissions': forms.CheckboxSelectMultiple
    }
