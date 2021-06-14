from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from app6.models import DiyUser

def user_reg(request):
    if request.method=="GET":
        return render(request,'6/user_reg.html')
    if request.method=="POST":
        uname=request.POST.get("username",'')
        pwd=request.POST.get("password",'')
        if User.objects.filter(username=uname):
            info='用户已经存在'
        else:
            d=dict(username=uname,password=pwd,email='111@111.com',is_staff=1,is_active=1,is_superuser=1)
            user=User.objects.create_user(**d)
            info='注册成功,请登陆'
        return render(request,'6/user_reg.html',{"info":info})

def diy_reg(request):
    if request.method=="GET":
        return render(request,'6/reg.html')
    if request.method=="POST":
        uname=request.POST.get("username",'')
        pwd=request.POST.get("password",'')
        if DiyUser.objects.filter(username=uname):
            info='用户已经存在'
        else:
            d=dict(username=uname,password=pwd,email='222@111.com',is_staff=1,is_active=1,is_superuser=1,weChat='yangcoder',level='1')
            user=DiyUser.objects.create_user(**d)
            info='注册成功,请登陆'
        return render(request,'6/reg.html',{"info":info})

def loginView(request):
    if request.method=="GET":
        return render(request,'6/login.html')
    if request.method=="POST":
        uname=request.POST.get("username",'')
        pwd=request.POST.get("password",'')
        if User.objects.filter(username=uname): #判断用户是否存在
            #如果存在，进行验证
            user=authenticate(username=uname,password=pwd)
            if user: #如果验证通过
                if user.is_active: #如果用户状态为激活
                    login(request,user) #进行登陆操作，完成session的设置
                    info="登陆成功"
                else:
                    info="用户还未激活"
            else:
                info="账号密码不对，请重新输入"
        else:
            info='用户账号不存在，请查询'
        return render(request,'6/login.html',{"info":info})

from django.shortcuts import redirect
def diy_loginView(request):
    if request.method=="GET":
        return render(request,'6/login.html')
    if request.method=="POST":
        uname=request.POST.get("username",'')
        pwd=request.POST.get("password",'')
        if DiyUser.objects.filter(username=uname): #判断用户是否存在
            #如果存在，进行验证
            user=authenticate(username=uname,password=pwd)
            if user: #如果验证通过
                if user.is_active: #如果用户状态为激活
                    login(request,user) #进行登陆操作，完成session的设置
                    info="登陆成功"
                    return redirect('/userbaseinfo_add')
                    #next=request.GET.get("next")
                    #if next:
                    #    print("http://"+request.get_host()+next)
                    #    return HttpResponseRedirect("http://"+request.get_host()+next)
                else:
                    info="用户还未激活"
            else:
                info="账号密码不对，请重新输入"
        else:
            info='用户账号不存在，请查询'
        return render(request,'6/login.html',{"info":info})

from django.contrib.auth.decorators import login_required, permission_required
@login_required
@permission_required("add_userbaseinfo")
def userbaseinfo_add(request):
    if request.method=="GET":
        return HttpResponse("进行新增操作")
    if request.method=="POST":
        #接收数据
        #保存
        pass
    