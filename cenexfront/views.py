from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import UserInfo
from django.contrib import messages
def home(request):
    return render(request,'cenexfront/home.html')
def about(request):
    return render(request,'cenexfront/about.html')
def service(request):
    return render(request,'cenexfront/service.html')
def contact(request):
    return render(request,'cenexfront/contact.html')
def booking(request):
    if request.user.is_authenticated:
        dict_cons={
            'UserInfo':UserInfo.objects.all()
        }
    else:
        return redirect('login')
    return render(request,'cenexfront/booking.html')
def signuppage(request):
    if request.method == 'POST':
        company_name=request.POST.get('comname')
        mobile_no=request.POST.get('phone')
        address=request.POST.get('address')
        pincode=request.POST.get('pincode')
        password=request.POST.get('password')
        myuser=User.objects.create_user(username=company_name,password=password)
        myuser.save()
        userinfo=UserInfo.objects.create(company_name=company_name,mobile_no=mobile_no,address=address,pincode=pincode)
        userinfo.save()
        return redirect('login')
    return render(request,'cenexfront/signup.html')
def loginpage(request):
    if request.method == 'POST':
        username=request.POST.get('comname')
        password=request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:    
            login(request,user)
            return redirect('booking')
        else:
            messages.error(request,"Invalid credentials")
            return redirect('login')
    return render(request,'cenexfront/login.html')
def logoutpage(request):
    logout(request)
    return redirect('login')