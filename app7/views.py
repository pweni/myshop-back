from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse,JsonResponse
from app7.models import *
import json

class GoodsListView(View):
    def get(self,request):
        """
        商品列表页
        """
        json_list=[]
        goods=Goods.objects.all()[:20]
        for good in goods:
            json_dict={}
            json_dict["name"]=good.name
            json_dict["market_price"]=good.market_price.to_eng_string()
            json_dict["price"]=good.price.to_eng_string()
            json_dict["unit"]=good.unit
            json_dict["click_num"]=good.click_num
            json_dict["amount"]=good.amount
            json_dict["stock_num"]=good.stock_num
            json_dict["fav_num"]=good.fav_num
            json_dict["goods_desc"]=good.goods_desc
            json_dict["main_img"]=str(good.main_img)
            json_dict["category_id"]=good.category.name
            json_list.append(json_dict)
        
        return HttpResponse(json.dumps(json_list,ensure_ascii=False, indent=4),content_type="application/json")
        #return JsonResponse(json_list,safe=False,json_dumps_params={'ensure_ascii':False,"indent":4})

class GoodsListView_JsonResponse(View):
    def get(self,request):
        """
        商品列表页
        """
        json_list=[]
        goods=Goods.objects.all()[:20]
        for good in goods:
            json_dict={}
            json_dict["name"]=good.name
            json_dict["market_price"]=good.market_price.to_eng_string()
            json_dict["price"]=good.price.to_eng_string()
            json_dict["unit"]=good.unit
            json_dict["click_num"]=good.click_num
            json_dict["amount"]=good.amount
            json_dict["stock_num"]=good.stock_num
            json_dict["fav_num"]=good.fav_num
            json_dict["goods_desc"]=good.goods_desc
            json_dict["main_img"]=str(good.main_img)
            json_dict["category_id"]=good.category.name
            json_list.append(json_dict)
        return JsonResponse(json_list,safe=False,json_dumps_params={'ensure_ascii':False,"indent":4})

from app7.serializers import GoodsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
class GoodsView(APIView):
    def get(self,request):
        #获取queryset
        goods=Goods.objects.all()[:10]
        #开始序列化
        goods_json=GoodsSerializer(goods,many=True)
        #返回序列化对象。goods_json.data是序列化后的值
        print(goods_json.data)
        return Response(goods_json.data)
    
    def post(self,request):
        data=request.data
        ser_data=GoodsSerializer(data=data,many=False)
        if ser_data.is_valid():
            goods=ser_data.save()
            return Response(ser_data.data)
        else:
            return Response(ser_data.errors)

from rest_framework import mixins
from rest_framework import generics
class GoodsListView_mixins(mixins.ListModelMixin,generics.GenericAPIView):
    queryset=Goods.objects.all()
    serializer_class=GoodsSerializer
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

class GoodsListView_List(generics.ListAPIView):
    queryset=Goods.objects.all()
    serializer_class=GoodsSerializer
     
    
