from django.contrib import admin
from django.urls import path,include
from app6 import views

urlpatterns = [
    path('user_reg/',views.user_reg),
    path('login/',views.loginView),
    path('diy_reg',views.diy_reg),
    path('diy_login/',views.diy_loginView),
    path('userbaseinfo_add',views.userbaseinfo_add),
]
