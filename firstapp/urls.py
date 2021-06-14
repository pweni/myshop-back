from django.contrib import admin
from django.urls import path,include
from firstapp import views

urlpatterns = [
    path('test/',views.test),
    path('index/',views.index),

    path('test_response/',views.test_response),

    path('var/',views.var),
    path('for_label/',views.for_label),
    path('filter/',views.filter),
    path('html_filter/',views.html_filter),
    path('welcome/',views.welcome),
    path('show_userinfo/',views.show_userinfo),
    path('add_userinfo/',views.add_userinfo),
    path('diy_filter/',views.diy_filter),
    path('diy_tags/',views.diy_tags),
    path('show_info/',views.show_info),

    #path('list/',views.list),
    #path('list_table/',views.list_table),
    #path('testform',views.testform),
    #path('userbaseinfoform',views.userbaseinfoform),
    path('userinfo_trans',views.userinfo_trans),
]
