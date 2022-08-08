from django.db import reset_queries
from django.shortcuts import redirect, render,HttpResponse
from datetime import datetime
from django.contrib.auth import authenticate
from django.contrib.auth import logout,login


# from django.contrib import messages

# Create your views here.
# def index(request):
#     context  = {
#         "variable1":"this is sent",
#         "variable2":"this is great"
#     }
#     return render(request,'index.html',context)
    # return HttpResponse("this is home page")

# def about(request):
#     return render(request,"about.html")


def index(request):
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request,'ls.html')


def loginuser(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return render(request,'login.html')
    return render(request,'login.html')      

def logoutuser(request):
    logout(request)
    return render(request,'login.html')  



