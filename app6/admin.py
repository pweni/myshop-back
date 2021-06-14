from django.contrib import admin
from app6.models import *
@admin.register(DiyUser)
class DiyUserAdmin(admin.ModelAdmin):
    list_display=['username','email','is_active','weChat','level']