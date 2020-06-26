from django.urls import path
from users import views
from users.views import welcome, mySpace, register, login, logout

urlpatterns = [
    path('', views.welcome),
    path('mySpace', views.mySpace),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
]