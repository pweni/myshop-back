from django.contrib import admin
from django.urls import path,include
from app5 import views

urlpatterns = [
    path('testform',views.testform),
    path('userbaseinfoform',views.userbaseinfoform),
    path('userinfoform',views.userinfo_form),
    path('userinfomsgform',views.userinfo_msg_form),
    path('widgetform',views.widgetform),

    path('userinfomodelform',views.userbaseinfo_modelform),
    path('modelform_user_save',views.modelform_user_save),

    path('ajax_login/',views.ajax_login),
    path('ajax_login_data/',views.ajax_login_data),
]
