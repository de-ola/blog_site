from .views import *
from django.urls import path

urlpatterns = [
    path('sign_up/', register, name="register"),
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),
]