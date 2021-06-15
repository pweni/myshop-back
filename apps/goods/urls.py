from django.urls import path,include
from apps.goods import views

urlpatterns = [
    path('index/',views.GoodsListView.as_view()),
    path('goods/',views.GoodsList.as_view()),
]
