from django import forms
from inside.models import User
from .models import UserProfileInfo
from django.contrib.auth.models import User as UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import TextInput

class FormRegister(forms.ModelForm):
    name = forms.CharField(label='Your name', max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    confirm = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['name', 'email', 'password']

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())

    class Meta():
        model = UserAdmin
        fields = ('username', 'email', 'password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('first_name','last_name','portfolio_site','profile_pic')

class UserUpdateForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ('first_name', 'last_name','email',)
        widgets = {
            'first_name': TextInput(attrs={'class': 'input', 'placeholder': 'First Name','help_text':'Optional.'}),
            'last_name' : TextInput(attrs={'class': 'input','placeholder':'Last Name','help_text':'Optional.'}),
            'email'     : TextInput(attrs={'class': 'input','placeholder':'Email', 'help_text':'Required. Inform a valid email address.'}),
            'username'  : TextInput(attrs={'class': 'input','placeholder':'Username'}),
        }
