from django.shortcuts import render
def home(request):
    return render(request,'cenexfront/home.html')