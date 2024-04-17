from django.shortcuts import render,redirect
from .forms import RegistrationForm
from .models import Account,MyaccountManager
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
# Create your views here.
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from carts.models import Cart,cartItem
from carts.views import _cart_id


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split("@")[0]
            # confirm_password = form.cleaned_data['confirm_password']

            user = Account.objects.create_user(first_name = first_name,last_name = last_name,phone_number= phone_number,email=email,password=password,username = username)
            user.save()
            # last_login = user.last_login if user.last_login else None
            # current_site = get_current_site(request)
            # mail_subject = ' Please activate your account'
            # message = render_to_string('account_verification_email.html',{
            #     'user':user,
            #     'domain': current_site,
            #     'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            #     'token':default_token_generator.make_token(user)

            # })
            # to_email = email
            # send_email = EmailMessage(mail_subject,message,to=[to_email])
            # send_email.send()
            messages.success(request,'Registration Successful')
            return redirect('register')
    else:
        form = RegistrationForm()
    context =  {
            'form':form
    }
    return render(request,'register.html',context)

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password  = request.POST['password']
        
        user = auth.authenticate(email=email,password=password)

        if user is not None:
            try:
                cart = Cart.objects.get(cart_id = _cart_id(request))
                is_cart_item_exists = cartItem.objects.filter(cart=cart).exists()
                if is_cart_item_exists:
                    cart_item = cartItem.objects.filter(cart=cart)
                    for item in cart_item:
                        item.user = user
                        item.save()
            except:
                pass
            auth.login(request,user)
            messages.success(request,'You are now logged in.')
            return redirect('home')
        else:
            messages.error(request,'Invalid login credentials')
            return redirect('login')

    return render(request,'signin.html')

@login_required(login_url = 'login')
def logout(request):
    auth.logout(request)
    messages.success(request,'You are logged out')
    return redirect('login')


# def activate(request):
#     return render(request,'account_verification_email.html')

def dashboard(request):
    return render(request,'dashboard.html')

def forgotpassword(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if Account.objects.filter(email= email).exists():
            return render(request,'resetpassword.html')
        else:
            messages.error(request,'Account does not exist')
    return render(request,'forgotpassword.html')

# def resetpassword(request):
#     if request.method == 'POST':
#         email = request.POST('email')
#         if Account.objects.filter(email= email).exists():
#             user = Account.objects.get(email=email)
#             # Generate a new random password
#             # new_password = UserModel.objects.make_random_password()
#             # # Set the new password for the user
#             # user.password = make_password(new_password)
#             # user.save()
#             # You can notify the user about the new password via email or any other means here
#             # For example: send_password_reset_email(user.email, new_password)
#             messages.success(request, 'Password reset successfully.')
#             return redirect('login')  # Redirect to login page after password reset
#         else:
#             messages.error(request, 'Account does not exist')
#     return render(request, 'resetpassword.html')


from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Account

def resetpassword(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = Account.objects.get(email=email)
        except Account.DoesNotExist:
            messages.error(request, 'Account does not exist')
            return render(request, 'resetpassword.html')
        
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if password == confirm_password and len(password) > 7:
            # Set the new hashed password for the user
            user.password = make_password(password)
            user.save()
            messages.success(request, 'Password reset successfully.')
            return redirect('login')  # Redirect to login page after password reset
        else:
            if len(password) < 8:
                messages.error(request, 'Passwords length is lessthan 8')
            else:
                messages.error(request, 'Passwords do not match.')
    return render(request, 'resetpassword.html')

