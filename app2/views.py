from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import *

def index(request):
    return HttpResponse("app2中的index方法")

def url_reverse(request):
    #使用reverse方法反向解析
    print("views函数中使用reverse解析的结果："+reverse("app2_url_reverse"))
    return render(request,"2/url_reverse.html")

def show_id(request,id):
    return HttpResponse("app2中的show_id方法,参数为id,值为"+str(id))

def show_uuid(request,id):
    return HttpResponse("app2中的show_uuid方法,参数为id,值为"+str(id))

def show_slug(request,q):
    return HttpResponse("app2中的show_slug方法,参数为q,值为"+str(q))

def article_list(request,year):
    return HttpResponse("app2中的article_list方法,参数为year,指定4位，值为"+str(year))

def article_any(request,q):
    return HttpResponse("app2中的article_any方法,参数为q,任意位数整数，值为"+str(q))

def article_page(request,page,key):
    return HttpResponse("app2中的article_page方法,参数为page,任意数字，值为"+str(page)+" 参数key，字母数字下划线，值为"+key)


def test_get(request):
    print(request.get_host()) #域名+端口
    print(request.get_raw_uri()) #全部路径，包含参数
    print(request.path) #获取访问文件路径，不含参数
    print(request.get_full_path())#获取访问文件路径，包含参数
    print(request.method) #获取请求中的使用的HTTP方式(POST/GET)
    print(request.GET) #获取GET请求的参数
    print(request.META["HTTP_USER_AGENT"]) #用户浏览器的user-agent字符串
    print(request.META["REMOTE_ADDR"]) #客户端IP
    print(request.GET.get('username'))#获取get参数
    return HttpResponse("")

def test_post(request):
    print(request.method) #获取请求中的使用的HTTP方式(POST/GET)
    print(request.POST.get('username'))
    return render(request,'2/test_post.html')

def test_render(request):
    return render(request,'2/test_render.html',{'info':'hello django'},content_type='text/html')

def test_redirect(request):
    return redirect("https://www.phei.com.cn/")

def test_redirect_model(request,id):
    user=UserBaseInfo.objects.get(id=id)
    return redirect(user)

def userinfo(request,id):
    user=UserBaseInfo.objects.get(id=id)
    return HttpResponse("编号："+str(user.id)+" 姓名："+user.username)

def test_redirect_views(request,id):
    return redirect('app2_userinfo',id)

def index_page(request):
    if request.method == 'GET':
        return HttpResponse("get请求")
    elif request.method == 'POST':
        return HttpResponse("post请求")

from django.views import View
class IndexPageView(View):
    '''
    类视图
    '''
    def get(self, request):
        return HttpResponse("get请求")
    def post(self, request):
        return HttpResponse("post请求")
