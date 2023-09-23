from django.shortcuts import render
def home(request):
    return render(request,'cenexfront/home.html')
def about(request):
    return render(request,'cenexfront/about.html')
def service(request):
    return render(request,'cenexfront/service.html')
def contact(request):
    return render(request,'cenexfront/contact.html')
def booking(request):
    return render(request,'cenexfront/booking.html')
def signuppage(request):
    return render(request,'cenexfront/signup.html')
def loginpage(request):
    return render(request,'cenexfront/login.html')