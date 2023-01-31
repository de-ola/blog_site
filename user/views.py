from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .forms import UpdateUserProfile
from django.contrib.auth import login, logout

# Create your views here.
def login(response):
    if response.method == "POST":
        username = response.POST['username']
        password = response.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(response, user)
            return redirect('index')

        else:
            messages.info(response, "Incorrect credentials!!!")
            return redirect('login')

    else:
        return render(response, 'registration/login.html')

def register(response):
    if response.method == 'POST':
        username = response.POST['username']
        email = response.POST['email']
        password = response.POST['password1']
        password2 = response.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(response, "This email already exists in our database")
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(response, "This username already exists in our database")
                return redirect('register')

            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                #automatically login the new user
                user = auth.authenticate(username=username, password=password)
                auth.login(response, user)

                return redirect('edit_profile')

        else:
            messages.info(response, "The passwords do not match")
            return redirect('register')

    else:
        return render(response, 'user/register.html')

def logout(response):
    auth.logout(response)
    return redirect('index')