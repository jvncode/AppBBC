from django.shortcuts import render, redirect
from django.contrib.auth import logout as do_logout

from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from products.models import Product

def welcome(request):
    return redirect('/login')

def register(request):
    # Create empty authentication form
    form = UserCreationForm()
    form.fields['username'].help_text = None
    form.fields['password1'].help_text = None
    form.fields['password2'].help_text = None
    if request.method == "POST":
        # Add the data received to the form
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            # Creation of new user account
            user = form.save()
            if user is not None:
                do_login(request, user)
                return redirect('/')
    return render(request, "users/register.html", {'form': form})

def login(request):
    form = AuthenticationForm()
    if request.method == "POST":
        # Add the data received to the form
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Retrieval of validated credentials
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verification of user credentials
            user = authenticate(username=username, password=password)

            if user is not None:
                do_login(request, user)
                products_user_pub = len(Product.objects.filter(owner=request.user))
                products_users_pub = len(Product.objects.all())
                context = {
                    'user': user,
                    'products_user_pub': products_user_pub,
                    'products_users_pub': products_users_pub,
                }
                return render(request, 'users/mySpace.html', context)
    return render(request, "users/login.html", {'form': form})

def logout(request):
    do_logout(request)
    return redirect('/login')


class mySpace(View):

    def get(self, request):
        # If there is identification, it is redirected to the personal area
        if request.user.is_authenticated:
            products_user_pub = len(Product.objects.filter(owner=request.user))
            products_users_pub = len(Product.objects.all())
            context = {
                'products_user_pub': products_user_pub,
                'products_users_pub': products_users_pub,

            }
            return render(request, "users/mySpace.html", context)
        # In another case we redirect to the login
        else:
            return redirect('/login')
