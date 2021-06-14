from django.contrib import admin
from django.urls import path,include
from django.views.static import serve
from django.conf import settings
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index,name='index'),
    path('',include('app1.urls')),
    path('',include('app2.urls')),
    path('',include('app5.urls')),
    path('',include('app6.urls')),
    path('basic/',include('apps.basic.urls')),
    path('member/',include('apps.member.urls')),
]

#if not settings.DEBUG:
#urlpatterns += [path('^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT})]
