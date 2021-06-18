from django.contrib import admin
from django.urls import path,include
from django.views.static import serve
from django.conf import settings
from app7 import views

urlpatterns = [
    path('app7/goods/',views.GoodsView.as_view()),
]