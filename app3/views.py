from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
    return render(request,"login.html")
def reg(request):
    if request.method == 'POST':
        uname = request.POST['username']
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword=request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=uname).exists():
                messages.info(request,"username taken")
                return redirect('reg')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email taken")
                return redirect('reg')
            else:
                user=User.objects.create_user(username=uname,first_name=fname,last_name=lname,email=email,password=password)
                user.save();
                return redirect('login')
                print("user created")

        else:
            messages.info(request,"password not matching")
            return redirect('reg')
        return redirect('/')
    return render(request,"reg.html")
def logout(request):
    auth.logout(request)
    return redirect('/')