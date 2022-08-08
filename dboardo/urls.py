from django.contrib import admin
from django.urls import path
from dboardo import views

urlpatterns = [
    # path('',views.index,name='dboardo'),
    # path('about',views.about,name='about'),
    # path('services',views.services,name='services'),
    # path('contact',views.contact,name="contact us")
    path('',views.index,name="index"),
    path('login',views.loginuser,name="login"),
    path('logout',views.logoutuser,name="logout"),
]