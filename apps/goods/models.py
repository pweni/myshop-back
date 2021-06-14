from django.db import models

class Goods(models.Model):
    gid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    cid = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=20, blank=True, null=True)
    pv = models.PositiveIntegerField()
    amount = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()
    img = models.CharField(max_length=100)
    desc = models.CharField(max_length=255, blank=True, null=True)
    status = models.PositiveIntegerField()

    class Meta:
        managed = True
        db_table = 't_goods'

class GoodsCategory(models.Model):
    gc_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    parent_id = models.PositiveIntegerField()
    sort = models.PositiveIntegerField()
    add_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 't_goods_category'