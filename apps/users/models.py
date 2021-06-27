from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    nickname=models.CharField('qq',blank=True,max_length=50)
    mobile=models.CharField('手机号码',max_length=11,default="")
    user_img=models.ImageField("头像",upload_to="user_img",default="")

    def __str__(self):
        return self.username
    
    class Meta(AbstractUser.Meta):
        permissions=(
            ['check_myuser','审核用户信息'],
        )