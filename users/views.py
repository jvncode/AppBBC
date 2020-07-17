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
    # Creamos el formulario de autenticación vacío
    form = UserCreationForm()
    form.fields['username'].help_text = None
    form.fields['password1'].help_text = None
    form.fields['password2'].help_text = None
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = UserCreationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Creamos la nueva cuenta de usuario
            user = form.save()
            # Si el usuario se crea correctamente 
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "users/register.html", {'form': form})

def login(request):
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                products_user_pub = len(Product.objects.filter(owner=request.user))
                products_users_pub = len(Product.objects.all())
                context = {
                    'user': user,
                    'products_user_pub': products_user_pub,
                    'products_users_pub': products_users_pub,

                }
                return render(request, 'users/mySpace.html', context)

    # Si llegamos al final renderizamos el formulario
    return render(request, "users/login.html", {'form': form})

def logout(request):
    do_logout(request)
    return redirect('/login')


class mySpace(View):

    def get(self, request):
        # Si estamos identificados devolvemos la portada
        if request.user.is_authenticated:
            products_user_pub = len(Product.objects.filter(owner=request.user))
            products_users_pub = len(Product.objects.all())
            context = {
                'products_user_pub': products_user_pub,
                'products_users_pub': products_users_pub,

            }
            return render(request, "users/mySpace.html", context)
        # En otro caso redireccionamos al login
        else:
            return redirect('/login')

