from django.urls import path,include
from apps.member import views

urlpatterns = [
    path('index/',views.index),
    path('add/',views.add),
    path('edit/<id>/',views.edit),
    path('del/<id>/',views.delete),
    path('index_page',views.index_page),
    path("list",views.list),
    path("index_bttable/",views.index_bttable),
    path("ajax_member/",views.ajax_member),
]
