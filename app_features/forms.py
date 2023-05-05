from django import forms


from app_features.models import ImageModel

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = ("image",)
        

