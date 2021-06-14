from django.db import models
from django.utils import timezone
class UserBaseInfo(models.Model):
    id=models.AutoField(verbose_name='编号',primary_key=True)
    username = models.CharField(verbose_name='用户名称',max_length=30)
    password = models.CharField(verbose_name='密码',max_length=10)
    age=models.IntegerField(verbose_name="年龄",default=1)
    mobile=models.CharField(verbose_name="手机号码",max_length=11)
    status = models.CharField(verbose_name='状态',max_length=1)
    createdate = models.DateTimeField(verbose_name='创建日期',db_column='createDate',auto_now=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        managed=True
        verbose_name='人员基本信息'
        db_table = 'UserBaseInfo5'

class DepartInfo(models.Model):
    id=models.AutoField(verbose_name='编号',primary_key=True)
    departname = models.CharField(verbose_name='部门名称',max_length=30)
    createdate = models.DateTimeField(verbose_name='创建日期',db_column='createDate', default=timezone.now)

    def __str__(self):
        return str(self.id)

    class Meta:
        managed=True
        verbose_name='部门信息'
        db_table = 'DepartInfo5'

class UserExtraInfo(models.Model):
    id=models.AutoField(verbose_name='编号',primary_key=True)
    username = models.CharField(verbose_name='用户名称',max_length=30)
    truename = models.CharField(verbose_name='真实姓名',max_length=30)
    sex = models.IntegerField(verbose_name='性别')
    salary = models.DecimalField(verbose_name='薪水',max_digits=8, decimal_places=2)
    age = models.IntegerField(verbose_name='年龄',)
    department = models.CharField(verbose_name='部门',max_length=20)
    status = models.CharField(verbose_name='状态',max_length=1)
    createdate = models.DateTimeField(verbose_name='创建日期',db_column='createDate')
    memo = models.TextField(verbose_name='备注',blank=True, null=True)
    user=models.OneToOneField(UserBaseInfo,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

    class Meta:
        managed=True
        verbose_name='人员扩展信息'
        db_table = 'UserExtraInfo5'

class CardInfo(models.Model):
    id=models.AutoField(verbose_name='编号',primary_key=True)
    cardno = models.CharField(verbose_name='卡号',max_length=30)
    bank = models.CharField(verbose_name='所属银行',max_length=30)
    user=models.ForeignKey(UserBaseInfo,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

    class Meta:
        managed=False
        verbose_name='用户卡信息'
        db_table = 'CardInfo5'