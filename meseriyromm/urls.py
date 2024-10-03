from django.contrib import admin
from django.urls import path,include
from meseriyromm import views


urlpatterns = [
    path('meseros/',views.SERadicionales),
    path('meseros/registarservi/',views.registaradicionales),
    ]