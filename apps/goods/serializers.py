from rest_framework import serializers
from .models import *

class GoodsSerializer(serializers.Serializer):
    name=serializers.CharField(required=True,max_length=100)
    click_num=serializers.IntegerField(default=0)

class GoodsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Goods
        fields="__all__"

{
    "code":"200",
    "msg":"显示的消息",
    "data":{
        "id":1,
        "name":"test",
        "desc":"内容"
    }
}
