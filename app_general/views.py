from django.http import HttpRequest
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from app_features.models import Feature, Cart, CartItem

# Create your views here.

def index(request):
    features = Feature.objects.all()

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)


    context = {"features":features}
    return render(request, "app_general/index.html", context)


def base(request):
    return render(request, 'app_general/base.html')

def about(request):
    return render(request, 'app_general/about.html')

def feature2(request):
    return render(request, 'app_general/feature.html')




