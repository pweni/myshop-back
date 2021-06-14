from django.db import models

# Create your models here.
class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    member_id = models.IntegerField()
    goods_id = models.IntegerField()
    goods_name = models.CharField(max_length=100)
    goods_price = models.DecimalField(max_digits=10, decimal_places=2)
    goods_num = models.IntegerField()

    class Meta:
        managed = True
        db_table = 't_cart'

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_sn = models.IntegerField()
    pay_sn = models.IntegerField()
    member_id = models.IntegerField()
    username = models.CharField(max_length=50)
    add_time = models.IntegerField()
    payment_code = models.CharField(max_length=10)
    payment_time = models.IntegerField(blank=True, null=True)
    finnshed_time = models.IntegerField()
    quantity = models.IntegerField(blank=True, null=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_total = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    order_state = models.CharField(max_length=2)
    delete_state = models.IntegerField()
    order_from = models.CharField(max_length=1)

    class Meta:
        managed = True
        db_table = 't_order'


class OrderGoods(models.Model):
    order_goods_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    gid = models.IntegerField()
    goods_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()

    class Meta:
        managed = True
        db_table = 't_order_goods'


class OrderPay(models.Model):
    pay_id = models.AutoField(primary_key=True)
    pay_sn = models.IntegerField()
    buyer_id = models.IntegerField()
    api_pay_state = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 't_order_pay'