from django.urls import path
from users import views


urlpatterns = [
    path('', views.welcome),
    path('mySpace', views.mySpace.as_view(), name='my_space'),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
]