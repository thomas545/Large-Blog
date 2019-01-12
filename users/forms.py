from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username' ,'email' ,'password1', 'password2']

    ## delete help texts
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm,self).__init__(*args,**kwargs)

        for fieldname in ['username' , 'password1' , 'password2']:
            self.fields[fieldname].help_text = None

## Update Profile

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username' ,'email']
        help_texts = {
            'username':'Enter Username'
        }

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
