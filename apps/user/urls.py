from django.urls import path,include
from apps.user import views

urlpatterns = [
    path('login/',views.login),
    path('reg/',views.reg),
    path('logout/',views.logout),
]
