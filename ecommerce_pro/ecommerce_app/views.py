from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse 
from django.contrib.auth import authenticate, logout as django_logout, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
import pdb

@login_required
def home(request):
    user = request.user
    return render (request, 'home.html', {'user': user})

def Wellcome(request):
    return HttpResponse('Wellcome To Django Project')

def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        exemail = User.objects.filter(email=email)
        if not exemail:
            username = request.POST.get('username')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')
            if password == confirm_password:
                users = User.objects.create_user(username, email, password)
                users.first_name = first_name
                users.last_name = last_name
                users.save()
                return redirect (Signin)
            else:
                messages.warning(request, 'PASSWORD NOT MATCH')
                return redirect(register)
        else:
            messages.warning(request, 'EMAIL ALREADY EXISTS')
            return redirect(register)
    else:
        return render (request, 'register.html')


def Signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user =  authenticate(username=username, password=password)
        if user is not None:
            username = user.username
            login(request, user)
            return redirect(home)
        else:
            messages.error(request, 'EMAIL OR PASSWORD NOT CORRECT')   
            return redirect(Signin)
    else: 
        return render(request, 'login.html')


def logout(request):
    django_logout(request)
    messages.success(request, "Logout Successfully")
    return redirect(Signin)
        


def change_password(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        current_user = request.user
        if current_user is None:
            return redirect (Signin)
        if password == confirm_password:
            current_user.set_password(password)
            current_user.save()
            messages.success(request, 'Password Reset Successfully')
            return redirect(Signin)
        else:
            messages.error(request, 'Password Not Match')
            return render(request, 'reset_password.html')
    else:
        return render(request, 'reset_password.html')