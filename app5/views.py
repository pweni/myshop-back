from django.http import HttpResponse, JsonResponse
from django.db import connection, transaction
from django.db.models import F
from .forms import *
from django.db import transaction
from django.db import connection
import json
from django.db.models import Q
from app5.models import *
import django.utils.timezone as timezone
from django.shortcuts import render
from django.http import HttpResponse
import datetime

def index(request):
    return render(request, 'index.html')

def testform(request):
    if request.method == "GET":
        myform = TestForm()
        return render(request, "5/testform.html", {'myform': myform})
    else:
        f = TestForm(request.POST)
        if f.is_valid():
            print(f["username"])
            print(f.cleaned_data["age"])
            # return "ok"
        else:
            error = f.errors
            print(error)
            return render(request, "5/testform.html", locals())


def widgetform(request):
    if request.method == "GET":
        myform = WidgetForm()
        return render(request, "5/testform.html", {'obj': myform})


def userbaseinfoform(request):
    if request.method == "GET":
        myform = UserBaseInfoForm()
        return render(request, "5/userbaseinfo.html", {'obj': myform})
    else:
        f = UserBaseInfoForm(request.POST)
        if f.is_valid():
            print(f.cleaned_data["username"])
            # print(f.cleaned_data["age"])
            # return "ok"
        else:
            errors = f.errors
            print(errors)
            return render(request, "5/userbaseinfo.html", {'obj': f, 'errors': errors})
        return render(request, "5/userbaseinfo.html", {'obj': f})


def userinfo_form(request):
    if request.method == "GET":
        myform = UserInfoForm()
        return render(request, "5/userinfo.html", {'form_obj': myform})


def userinfo_msg_form(request):
    if request.method == "GET":
        myform = UserInfo_Msg_Form()
        return render(request, "5/userinfoform.html", {'form_obj': myform})
    else:
        f = UserInfo_Msg_Form(request.POST)
        if f.is_valid():
            print(f.clean())
            print(f.cleaned_data["username"])
            print(f.data)
        else:
            errors = f.errors
            print(errors)
            return render(request, "5/userinfoform.html", {'form_obj': f, 'errors': errors})
        return render(request, "5/userinfoform.html", {'form_obj': f})


def userbaseinfo_modelform(request):
    if request.method == "GET":
        myform = UserBaseInfoModelForm()
        return render(request, "5/userinfoform.html", {'form_obj': myform})
    else:
        f = UserBaseInfoModelForm(request.POST)
        if f.is_valid():
            print(f.clean())
            print(f.cleaned_data["username"])
            print(f.data)
        else:
            errors = f.errors
            print(errors)
            return render(request, "5/userinfoform.html", {'form_obj': f, 'errors': errors})
        return render(request, "5/userinfoform.html", {'form_obj': f})

def modelform_user_save(request):
    if request.method == "GET":
        a=UserBaseInfo.objects.get(id=1)
        myform = UserBaseInfoModelForm(instance=a)
        return render(request, "5/userinfoform.html", {'form_obj': myform})
    else:
        f = UserBaseInfoModelForm(request.POST)
        if f.is_valid():
            f.save()
        else:
            errors = f.errors
            print(errors)
            return render(request, "5/userinfoform.html", {'form_obj': f, 'errors': errors})
        return render(request, "5/userinfoform.html", {'form_obj': f})

def userinfo_set_form(request):
    if request.method == "GET":
        id = request.GET.get("id", "")
        if id:
            UserBaseInfo.objects.filter(id=id)

        myform = UserBaseInfoForm()
        return render(request, "5/userbaseinfo.html", {'myform': myform})
    else:
        f = UserBaseInfoForm(request.POST)
        if f.is_valid():
            print(f["username"])
            print(f.cleaned_data["age"])
            return "ok"
        else:
            error = f.errors
            print(error)
            return render(request, "5/userbaseinfo.html", locals())

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def ajax_login(request):
    return render(request,"5/ajax.html")
@csrf_exempt
def ajax_login_data(request):
    # 获取用户名和密码
    username = request.POST.get('username')
    password = request.POST.get('password')
    # 判断并返回json数据
    if username == 'admin' and password == '123456':
        return JsonResponse({'code': 1,"msg":"登陆成功"})
    else:
        return JsonResponse({'code': 0,"msg":"登陆失败"})
