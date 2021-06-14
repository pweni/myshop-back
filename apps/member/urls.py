from django.urls import path,include
from apps.member import views

urlpatterns = [
    path('index',views.index),
    path('index_page',views.index_page),
]
