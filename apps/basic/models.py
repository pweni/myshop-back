from django.db import models

# Create your models here.
class Address(models.Model):
    address_id = models.AutoField(primary_key=True)
    member_id = models.PositiveIntegerField()
    true_name = models.CharField(max_length=50)
    area_id = models.PositiveIntegerField()
    city_id = models.IntegerField()
    area_info = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    mobilephone = models.CharField(max_length=15, blank=True, null=True)
    is_default = models.IntegerField()

    class Meta:
        managed = True
        db_table = 't_address'

class Area(models.Model):
    area_id = models.AutoField(primary_key=True)
    area_name = models.CharField(max_length=50)
    area_parent_id = models.PositiveIntegerField()
    area_sort = models.PositiveIntegerField()

    class Meta:
        managed = True
        db_table = 't_area'