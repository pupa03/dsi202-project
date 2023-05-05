from django.contrib.auth.forms import UserCreationForm,  AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from app_users.models import Profile, CustomUser


class RegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}),max_length=12,required=True)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'ConfirmPassword'}))
    class Meta:
        model = CustomUser
        fields = ("username", "email", "password1", "password2")



class UserProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name")

class ExtendedProfileForm(forms.ModelForm):
    prefix = "extended"
    
    class Meta:
        model = Profile
        fields = ("address", "phone")
        labels = {
            "address": "ที่อยู่",
            "phone": "เบอร์โทรศัพท์",
        }
        widgets = {
            "address": forms.Textarea(attrs={"rows": 3})
        }