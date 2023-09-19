from django.shortcuts import render
def home(request):
    return render(request,'cenexfront/home.html')
def about(request):
    return render(request,'cenexfront/about.html')
def service(request):
    return render(request,'cenexfront/service.html')
def contact(request):
    return render(request,'cenexfront/contact.html')