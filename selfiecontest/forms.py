from django import forms

from .models import SignUp,Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

class ContactForm(forms.Form):
    full_name=forms.CharField()
    email=forms.EmailField()
    message=forms.CharField(widget=forms.Textarea)

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields= ['full_name','email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        return email
    def clean_full_name(self):
        full_name=self.cleaned_data.get('full_name')
        return full_name


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('college', 'city', 'pic',)
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')