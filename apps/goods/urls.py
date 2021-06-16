from django.urls import path,include
from apps.goods import views

urlpatterns = [
    path('index/',views.GoodsListView.as_view()),
    path('goods/',views.GoodsList.as_view()),

    path('goods_mixin/',views.GoodsListView_mixins.as_view()),
    path('goods_list/',views.GoodsListView_List.as_view()),
]
