from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

def register(request):
    if(request.method=="POST"):
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
       
        if(password==confirm_password):
            user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
            user.save()
            return redirect('shop:cate')
        else:
            return HttpResponse("Password are not same")
    return render(request,'register.html')


def user_login(request):
    if(request.method=="POST"):
        username = request.POST['username']
        password = request.POST['password']
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('shop:cate')
        else:
            return HttpResponse("Invalid credentials")

    return render(request,'login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('authentication:log')