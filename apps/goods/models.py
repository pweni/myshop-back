from django.db import models
from datetime import datetime
from common.base_model import BaseModel

class GoodsCategory(BaseModel):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=50,verbose_name='分类名称',default='')
    parent=models.ForeignKey("self", null=True,blank=True,verbose_name="父类",on_delete=models.DO_NOTHING)
    logo=models.ImageField(verbose_name="分类logo图片",upload_to="uploads/goods_img/")
    sort=models.IntegerField(verbose_name='排序')
    #create_time=models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    #update_time=models.DateTimeField(auto_now=True,verbose_name="更新时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='商品分类'
        db_table='d_goods_category'

class Goods(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,verbose_name='商品名称',default='')
    category=models.ForeignKey(GoodsCategory,blank=True,null=True,verbose_name='商品分类',on_delete=models.DO_NOTHING)
    market_price = models.DecimalField(max_digits=8,default=0, decimal_places=2,verbose_name='市场价格')
    price = models.DecimalField(max_digits=8, decimal_places=2,default=0,verbose_name='实际价格')
    unit=models.CharField(max_length=10,verbose_name='计量单位',blank=True,null=True)
    click_num = models.IntegerField(default=0, verbose_name="点击数")
    amount = models.IntegerField(default=0, verbose_name="销售量")
    stock_num = models.IntegerField(default=0, verbose_name="库存数")
    fav_num = models.IntegerField(default=0, verbose_name="收藏数")
    goods_desc=models.CharField(max_length=5000,verbose_name='商品描述',default='')
    main_img=models.ImageField(verbose_name='商品主图',blank=True,null=True,upload_to='goods/images/')
    createDate=models.DateTimeField(default=datetime.now,verbose_name='创建时间')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name='商品'
        db_table = 'd_goods'