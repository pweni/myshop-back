from django.urls import path,re_path
from app2 import views
from app2.views import IndexPageView
from app2.views_class import *

urlpatterns = [
    path('app2/index/',views.index,name='app2_index'),
    path('app2/url_reverse/',views.url_reverse,name='app2_url_reverse'),
    path('app2/show/<int:id>/',views.show_id,name='show_id'),
    path('app2/article/<uuid:id>/',views.show_uuid,name='show_uuid'),
    path('app2/article/<slug:q>/',views.show_slug,name='show_slug'),

    re_path('^app2/list/(?P<year>\d{4})/$', views.article_list),
    re_path('^app2/page/(?P<page>\d+)&key=(?P<key>\w+)',views.article_page,name="article_page"),

    path('app2/test_get/',views.test_get),
    path('app2/test_post/',views.test_post),
    path('app2/test_render/',views.test_render,name='app2_test_render'),
    path('app2/test_redirect/',views.test_redirect,name='app2_test_redirect'),

    path('app2/test_redirect_model/<int:id>/',views.test_redirect_model,name='app2_test_redirect_model'),
    path('app2/userinfo/<int:id>/',views.userinfo,name='app2_userinfo'),
    path('app2/test_redirect_views/<int:id>/',views.test_redirect_views,name='app2_test_redirect_views'),

    path('indexpage',IndexPageView.as_view()),

    path('app2/test_templateview/',TestTemplateView.as_view())






]
