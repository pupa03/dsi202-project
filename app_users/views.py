from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.conf import settings


from app_users.forms import ExtendedProfileForm, RegisterForm, UserProfileForm
from app_users.models import  CustomUser
from app_users.utils.activation_token_generator import activation_token_generator

# Create your views here.


def register(request: HttpRequest):
    #POST
    if request.method=="POST" :
        form = RegisterForm(request.POST)
        password = request.POST['password1']
        confirm_password = request.POST['password2']
        if password != confirm_password:
            messages.warning(request,"Password is Not Matching")
            return redirect(reverse('register'))
        
        elif form.is_valid():
            # Register user

            user: CustomUser = form.save(commit=False)
            user.is_active = False
            user.save()

            #login(request, user)

            # Build email body HTML
            context = {
                "protocol": request.scheme,
                "host": request.get_host(),
                "uidb64": urlsafe_base64_encode(force_bytes(user.id)),
                "token": activation_token_generator.make_token(user)
            }
            email_body = render_to_string("app_users/activate_email.html", context)



            # Send Email
            email_message = EmailMessage(
                subject="Activate account",
                body=email_body,
                #from_email=settings.EMAIL_HOST_USER,
                to=[user.email], 
            )
            email_message.send()

            #if timestamp
                

            # Redirect to thankyou
            return redirect(reverse("register_thankyou"))
    
    #GET
    else:
        form = RegisterForm()
    context = {"form":form}
    return render(request, "app_users/register.html", context)

#Change?? ====
def handlelogin(request: HttpRequest):
    if request.method=="POST":
        useremail = request.POST('email')
        userpassword = request.POST('pass1')
        myuser = authenticate(username=useremail, password=userpassword)
        userpassword = CustomUser.objects.get(all)
        if useremail is None:
            messages.warning(request,"User not exist")
            return redirect(reverse('handlelogin'))
    return render(request, "registration/login.html")



def register_thankyou(request: HttpRequest):
    return render(request, "app_users/register_thankyou.html")



def activate(request: HttpRequest, uidb64: str, token: str):
    title = "Activate account เรียบร้อย"
    description = "คุณสามารถเข้าสู่ระบบได้เลย"

    # Decode user id
    id = urlsafe_base64_decode(uidb64).decode()

    try:
        user: CustomUser = CustomUser.objects.get(id=id)
        if not activation_token_generator.check_token(user, token):
            raise Exception("Check token false")
        user.is_active = True
        user.save()
    except:
        print("Activate ไม่ผ่าน")
        title = "Activate account ไม่ผ่าน"
        description = "ลิ้งค์อาจถูกใช้ไปแล้ว หรือหมดอายุ"
        #Activate agian?

    context = {"title": title, "description": description}
    return render(request, "app_users/activate.html", context)



@login_required
def dashboard(request: HttpRequest):
    favorite_food_pivots = request.user.favorite_food_pivot_set.order_by("-level")
    context = {"favorite_food_pivots": favorite_food_pivots}
    return render(request, "app_users/dashboard.html", context)



@login_required
def profile(request: HttpRequest):
    user = request.user
    #POST
    if request.method=="POST":
        form = UserProfileForm(request.POST, instance=user)
        is_new_profile = False

        try:
            #Will update
            extended_form = ExtendedProfileForm(request.POST, instance=user.profile)
        except:
            #Will create
            extended_form = ExtendedProfileForm(request.POST)
            is_new_profile = True

        if form.is_valid() and extended_form.is_valid():
            form.save()
            if is_new_profile:
                #Create
                profile = extended_form.save(commit=False)
                profile.user = user
                profile.save()
            else:
                #Update
                extended_form.save()

            response = HttpResponseRedirect(reverse("profile"))
            response.set_cookie("is_saved", "1")
            return response
        
    else:
        form = UserProfileForm(instance=user)
        try:
            extended_form = ExtendedProfileForm(instance=user.profile)
        except:
            extended_form = ExtendedProfileForm()

    #GET
    is_saved = request.COOKIES.get("is_saved") == "1"
    flash_message = "บันทึกเรียบร้อย" if is_saved else None
    form = UserProfileForm()
    extended_form = ExtendedProfileForm()
    context = {
        "form": form,
        "extended_form": extended_form,
        "flash_message": flash_message,
    }
    response = render(request, "app_users/profile.html", context)
    if is_saved:
        response.delete_cookie("is_saved")
    return response

