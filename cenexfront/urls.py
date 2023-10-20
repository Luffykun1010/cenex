from . import views
from django.urls import path,include
urlpatterns = [
    path('',views.home,name='home'),
    path('home',views.home,name='home'),
    path('about',views.about,name='about'),
    path('service',views.service,name='service'),
    path('contact',views.contact,name='contact'),
    path('booking',views.booking,name='booking'),
    # path('signup',views.signuppage,name='signup'),
    # path('login',views.loginpage,name='login'),
    # path('logout',views.logoutpage,name='logout'),
]