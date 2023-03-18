from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as django_login
from django.contrib import messages
from django.db import IntegrityError

# Create your views here.
def signup(request):
    if request.method == 'POST':
        try:

            first_name=request.POST.get("first_name")
            last_name=request.POST.get("last_name")
            email=request.POST.get("email")
            password=request.POST.get("password")
            username=request.POST.get("username")
            
            print(first_name)
            print(last_name)
            print(email)
            print(password)
            print(username)

            user = User.objects.create_user(username=username, first_name=first_name , last_name=last_name, password=password, email=email )
            messages.success(request, "Account created")
        
            return redirect('/authentication/login/')
        except IntegrityError:
            messages.error(request,"Username or email already taken")
    context = {
        "document_title" : "signup",
    }
    return render(request,'authentication/signup_form.html',context)

def login(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
    

        user=authenticate(username=username, password=password)


        if user is not None:
            django_login(request, user)
            return redirect('/dashboard/')
        else:
            messages.error(request,"Account does not exist")
            print('User not found')
    context = {
        "document_title" : "login",
        
    }
    return render(request, 'authentication/login_form.html',context)