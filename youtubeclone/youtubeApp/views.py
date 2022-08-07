from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate

# Create your views here.

def index(request):
    return render(request,'youtubeapp/index.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['confirm_password']
        if  password != cpassword:
            messages.warning(request,''' Password doesn't match''')
            return redirect("signup")
        else:
            if name and email and password:
                a=User.objects.create_user(name,email,password)
                if a:
                    return redirect("index")

    return render(request,'youtubeapp/auth/signup.html',{})

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect("index")
        else:
            messages.warning(request,''' wrong username or password ''')
            return redirect("signin")
    return render(request,'youtubeapp/auth/signin.html',{})