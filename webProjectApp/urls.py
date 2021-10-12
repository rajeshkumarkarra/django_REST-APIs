from django.contrib import admin
from django.urls import path
from webProjectApp import views

urlpatterns = [
    path('home_view/', views.home_view, name ='home'),
]