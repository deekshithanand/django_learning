from django.shortcuts import render, redirect,HttpResponse
from django.contrib import messages, auth
from django.contrib.auth.models import User
# Create your views here.


def register(request):
    if request.method == 'POST':
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        uname = request.POST['username']
        email = request.POST['username']
        pwd = request.POST['password']
        cpwd = request.POST['password2']

        if pwd == cpwd:
            if User.objects.filter(username=uname).exists():
                messages.error(request, 'Username exists')
                return render(request, "register")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email already taken!")
            else:
                user = User.objects.create_user(
                    username=uname, email=email, password=pwd)
                user.save()
                messages.success(request, "User Registered!")
                return redirect("login")
        else:
            messages.error(request, "Passwords dont match!")
            return render(request, "register.html")
        # logic to save user
    if request.method == 'GET':
        return render(request, "register.html")


def login(request):
    if request.method == 'POST':
        uname = request.POST['username']
        pwd = request.POST['password']

        user = auth.authenticate(username = uname,password = pwd)

        if user is not None:
            auth.login(request,user)
            messages.success(request,"Logged in successfully!")
            return render(request,'base.html')
        else:
            messages.error(request,"Invalid Credentials!")
            return redirect("login")


    if request.method == 'GET':
        auth.logout(request)
        return render(request, "login.html")


def logout(request):
    return "LOgout"


def dashboard(request):
    return dahsboard
