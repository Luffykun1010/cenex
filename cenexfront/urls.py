from . import views
from django.urls import path,include
urlpatterns = [
    path('',views.home,name='home'),
    path('home',views.home,name='home'),
    path('about',views.about,name='about'),
    path('service',views.service,name='service'),
]