from django.contrib.auth.forms import UserCreationForm,  AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from app_users.models import Profile, CustomUser


class RegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}),label="Username",label_suffix="",max_length=12,required=True)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),label="Email",label_suffix="",required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}),label="Password",label_suffix="",required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm Password'}),label="Confirm Password",label_suffix="",required=True)
    class Meta:
        model = CustomUser
        fields = ("username", "email", "password1", "password2")



class UserProfileForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Firstname'}),label="Firstname",label_suffix=" :",max_length=20)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Lastname'}),label="Lastname",label_suffix=" :",max_length=20)
    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name")



class ExtendedProfileForm(forms.ModelForm):
    address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address'}),label="Address",label_suffix=" :",max_length=100)
    phone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phonenumber'}),label="Phone",label_suffix=" :",max_length=10)

    prefix = "extended"

    class Meta:
        model = Profile
        fields = ("address", "phone")

