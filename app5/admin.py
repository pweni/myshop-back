from django.contrib import admin
from app5.models import *
@admin.register(UserBaseInfo)
class UserBaseInfoAdmin(admin.ModelAdmin):
    list_display=['username','age','mobile','status']
