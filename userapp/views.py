from django.shortcuts import render,redirect
from django.urls import path
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.
def register(request):
    if  request.method == "POST":
        user_name = request.POST["username"] 
        email = request.POST["email"] 
        pwd = request.POST["password"] 
        if user_name == "" or email =="" or pwd =="":
            messages.warning(request,"Please fill out of all input box")
            return redirect("/register")
        else:
           if User.objects.filter(username=user_name).exists():
            messages.warning(request,"This user is already exists")
            return redirect("/register")
           else:
            obj_user = User.objects.create_user(
                username=user_name,
                email=email,
                password=pwd  
                )
            obj_user.save()
            messages.success(request,"You have registered successfully...")
            return redirect("/register")

           
    else:
        return render(request,"register.html")
def login(request):
    pass
def logout(request):
    pass