from django.db import models
from datetime import datetime

class Member(models.Model):
    LEVEL=(
        (1,'寂寞卡会员'),
        (2,'钻石卡会员'),
        (3,'金卡会员'),
        (4,'银卡会员'),
    )

    member_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    truename = models.CharField(max_length=20, blank=True, null=True)
    logo = models.ImageField(max_length=50, upload_to="member_img",blank=True, null=True)
    sex = models.IntegerField(blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    passwd = models.CharField(max_length=32)
    email = models.CharField(max_length=100)
    mobile = models.CharField(max_length=11, blank=True, null=True)
    level=models.IntegerField(default=4,choices=LEVEL)
    status=models.IntegerField(default=0)
    create_time=models.DateTimeField(default=datetime.now,verbose_name='创建时间')
    update_time=models.DateTimeField(default=datetime.now,verbose_name="更新时间")

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'd_member'