from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


import json
from PIL import Image
import libscrc
import qrcode
from app_features.models import Feature, Cart, CartItem, ImageModel
from app_features.forms import CheckoutForm
from app_users.models import CustomUser

# Create your views here.


def feature(request):
    features = Feature.objects.all()

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)


    context = {"features":features}
    return render(request, "app_general/feature.html", context)


@login_required
def cart(request):

    cart = None
    cartitems = []

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
        cartitems = cart.cartitems.all()

    context = {"cart":cart, "items":cartitems}
    return render(request, "app_features/cart.html", context)


def add_to_cart(request):
    data = json.loads(request.body)
    feature_id = data["id"]
    feature = Feature.objects.get(id=feature_id)

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
        cartitem, created = CartItem.objects.get_or_create(cart=cart, feature=feature)
        cartitem.quantity += 1
        cartitem.save()

        num_of_item = cart.num_of_items

        print(cartitem)
        print(num_of_item)

    return JsonResponse(num_of_item, safe=False)


def remove_from_cart(request):
    data = json.loads(request.body)
    items_id = data["id"]
    item = CartItem.objects.get(id=items_id)

    if request.user.is_authenticated:
        cart = Cart.objects.get(user=request.user, completed=False)
        cartitem = CartItem.objects.get(id=items_id)
        print(cartitem)
        cartitem.quantity = (cartitem.quantity - 1)

    cartitem.save()

    if cartitem.quantity <= 0:
        cartitem.delete()


    return JsonResponse('Item was remove', safe=False)



def calculate_crc(code):
    crc = libscrc.ccitt_false(str.encode(code))
    crc = str(hex(crc))
    crc = crc[2:].upper()
    return crc.rjust(4, '0')


def gen_code(mobile="", nid="", amount=""):
    code="00020101021153037645802TH29370016A000000677010111"
    if mobile:
        tag,value = 1,"0066"+mobile[1:]
        seller='{:02d}{:02d}{}'.format(tag,len(value), value)
        print(seller)
    elif nid:
        tag,value = 2,nid
        seller='{:02d}{:02d}{}'.format(tag,len(value), value)
    else:
        raise Exception("Error: gen_code() does not get seller mandatory details")
    code+=seller
    tag,value = 54, '{:.2f}'.format(amount)
    code+='{:02d}{:02d}{}'.format(tag,len(value), value)
    code+='6304'
    code+=calculate_crc(code)
    return code


from IPython.display import Image

def get_qr(request,mobile="0863573091",nid="",amount=""):
    message="mobile: %s, nid: %s, amount: %s"%(mobile,nid,amount)
    print( message )
    code=gen_code(mobile=mobile, amount=float(amount))#scb
    print(code)
    img = qrcode.make(code,box_size=4)
    response = HttpResponse(content_type='image/png')
    img.save(response, "PNG")
    return response



@login_required
def checkout(request):
    cart = Cart.objects.get(user=request.user)
    price = cart.total_price
    print(price)
    print(type(price))

    #Upload Slip
    if request.method == "POST":
        print("POST")
        form = CheckoutForm(request.POST,request.FILES)
        if form.is_valid():
            print("valid form")
            image = form.cleaned_data.get("image")
            obj = ImageModel.objects.get(image=image)
            obj.save()
            print("ABC")
            print(obj)

            return redirect(reverse('checkout_thankyou'))
        
        else :
            print("WHY ERROR")
            print(form.errors.as_data())

    else:
        form = CheckoutForm()

    context={
        "mobile":"0863573091", #seller's mobile
        "amount": price,
        "form": form,
    }
    return render(request, 'app_features/checkout.html', context)


def checkout_thankyou(request):
    form = CheckoutForm()
    context = {"form":form}
    return render(request, 'app_features/checkout_thankyou.html', context)