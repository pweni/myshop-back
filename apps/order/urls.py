from django.contrib import admin
from django.urls import path,include
from apps.order import views

urlpatterns = [
    path('index/',views.index),
]
