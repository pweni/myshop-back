from django.contrib import admin
from django.urls import path,include,re_path
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('basic/',include('apps.basic.urls')),
    path('member/',include('apps.member.urls')),
    path('goods/',include('apps.goods.urls')),
    path('users/',include('apps.users.urls')),

    re_path('media/(?P<path>.*)', serve, {"document_root": settings.MEDIA_ROOT}),
]

#if not settings.DEBUG:
#urlpatterns += [path('^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT})]
