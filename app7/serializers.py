from rest_framework import serializers
from .models import *

class GoodsSerializer(serializers.Serializer):
    name=serializers.CharField(required=True,max_length=100)
    #category=serializers.ForeignKey(GoodsCategory,on_delete=models.DO_NOTHING)
    market_price =serializers.DecimalField(max_digits=8, decimal_places=2)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)

    def create(self, validated_data):
        print(type(validated_data),validated_data)
        return Goods.objects.create(**validated_data)

class GoodsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Goods
        fields="__all__"
