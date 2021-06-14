from django.db import models

# Create your models here.
class Member(models.Model):
    member_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    truename = models.CharField(max_length=20, blank=True, null=True)
    logo = models.CharField(max_length=50, blank=True, null=True)
    sex = models.IntegerField(blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    passwd = models.CharField(max_length=32)
    email = models.CharField(max_length=100)
    mobile = models.CharField(max_length=11, blank=True, null=True)
    add_time = models.CharField(max_length=10)

    class Meta:
        db_table = 'd_member'


class MemberToken(models.Model):
    token_id = models.AutoField(primary_key=True)
    member_id = models.PositiveIntegerField()
    username = models.CharField(max_length=50)
    token = models.CharField(max_length=50)
    login_time1 = models.PositiveIntegerField()
    client_type = models.CharField(max_length=10)

    class Meta:
        db_table = 't_member_token'