from django.db import models
class Member(models.Model):
    member_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    truename = models.CharField(max_length=20, blank=True, null=True)
    logo = models.ImageField(max_length=50, upload_to="member_img",blank=True, null=True)
    sex = models.IntegerField(blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    passwd = models.CharField(max_length=32)
    email = models.CharField(max_length=100)
    mobile = models.CharField(max_length=11, blank=True, null=True)
    add_time = models.CharField(max_length=10)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'd_member'