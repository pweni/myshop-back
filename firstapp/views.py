from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def index(request):
    return render(request,'index.html')

def test(request):
    return render(request,'test.html')

def hello(request):
    return HttpResponse("Hello Django!!!")

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
    return render(request,'test_post.html')

def test_response(request):
    response=HttpResponse()
    response.write("hello django")
    response.write("<br>")
    response.write(response.content)
    response.write("<br>")
    response.write(response['Content-type'])
    response.write("<br>")
    response.write(response.status_code)
    response.write("<br>")
    response.write(response.charset)
    response.write("<br>")
    return response


def test_response_img(request):
    #输出一幅图片
    f = open(r'e:/图片.jpg', 'rb')
    response = HttpResponse(f.read(), content_type='image/jpeg')
    return response

def var(request):
   #v=PersonInfo.objects.all()
   #print(v)
   #列表对象
   lists=['Java','Python','C','C#','JavaScript']
   #字典对象
   dicts={'姓名':'张三','年龄':25,'性别':'男'}

   return render(request,'var.html',{'lists':lists,'dicts':dicts})

def for_label(request):
   dict1={'书名':'Django开发','价格':80,'作者':'张三'}
   dict2={'书名':'Python开发','价格':90,'作者':'李四'}
   dict3={'书名':'Java开发','价格':100,'作者':'王五'}
   lists=[dict1,dict2,dict3]
   return render(request,'for_label.html',{'lists':lists})

def filter(request):
   #定义网址
   #url_addr="<table border=1><tr><td>这是一个表格</td></tr></table>";
   str1="abcdefg"
   str2="ABCDEFG"
   slice_str="1234567890"
   time_str=datetime.datetime.now()
   return render(request,'filter.html',{"str1":str1,"str2":str2,"slice_str":slice_str,"time_str":time_str})

def html_filter(request):
   html_addr="<table border=1><tr><td>这是一个表格</td></tr></table>"
   html_script="<script language='javascript'>document.write('非法执行');</script>"
   return render(request,'html_filter.html',{"html_addr":html_addr,"html_script":html_script})


def welcome(request):
   return render(request,'welcome.html')

def show_userinfo(request):
    users = UserInfo.objects.all()  # 查询数据表中的全部数据
    user_id = 1
    oneuser = UserInfo.objects.get(id=1)  # 查询id=1的数据
    return render(request, 'userinfo.html', {"users": users, "oneuser": oneuser})

def diy_tags(request):
   dict1={'标题':'学习Python的好方法就是每天不间断的写代码'}
   dict2={'标题':'学习Django的好方法就是上手做个项目比如CMS、OA等'}
   dict3={'标题':'学习新知识的好方法就是快速构建一颗知识树'}
   lists=[dict1,dict2,dict3]
   return render(request,'diy_tags.html',{'lists':lists})

def diy_filter(request):
   dict1={'标题':'学习Python的好方法就是每天不间断的写代码'}
   dict2={'标题':'学习Django的好方法就是上手做个项目比如CMS、OA等'}
   dict3={'标题':'学习新知识的好方法就是快速构建一颗知识树'}
   lists=[dict1,dict2,dict3]
   return render(request,'diy_filter.html',{'lists':lists})

def diy_tags(request):
   dict1={'标题':'学习Python的好方法就是每天不间断的写代码'}
   dict2={'标题':'学习Django的好方法就是上手做个项目比如CMS、OA等'}
   dict3={'标题':'学习新知识的好方法就是快速构建一颗知识树'}
   lists=[dict1,dict2,dict3]
   return render(request,'diy_tags.html',{'lists':lists})

def show_info(request):
   return render(request,'show_info.html')

def add_userinfo(request):
    users = UserInfo()
    try:
        users.username = "zhangsan"
        users.nickname = "张三"
        users.password = "123456"
        users.suoding = 1
        users.status = "5"
        users.memo = "这是备注"
        users.score = "90.5"
        users.save()
        return HttpResponse("数据新增成功")
    except Exception as e:
        return HttpResponse("数据新增失败")

        # users=UserInfo.objects.create(username="zhangsan",nickname="张三",password="123456",)

from firstapp.models import *
import django.utils.timezone as timezone
def add_depart(request):
    depart=DepartInfo()
    depart.departname="技术部"
    depart.createdate=timezone.now()
    depart.save()

def add_depart1(request):
    d=dict(departname="财务部",createdate=timezone.now())
    depart=DepartInfo.objects.create(**d)

def add_userbaseinfo(request):
    d=dict(username="张三",password='123456',status=1,createdate=timezone.now())
    depart=UserBaseInfo.objects.create(**d)

def add_userbaseinfo1(request):
    depart=UserBaseInfo.objects.create(username="张三",password='123456',status=1,createdate=timezone.now())

def add_userextrainfo(request):
    #添加用户基本表
    d=dict(username="李四",password='123456',status=1,
    createdate=timezone.now())
    userbaseinfo=UserBaseInfo.objects.create(**d)
    #添加用户扩展表
    d=dict(username="李四",truename='李小四',sex=0,salary=6555.88,age=35,
    status=0,createdate=timezone.now(),memo='',user=userbaseinfo)
    userextrainfo=UserExtraInfo.objects.create(**d)

def query_userinfo(request):
    userextrainfo=UserExtraInfo.objects.get(id=1)
    userextrainfo.user.username

    user=UserBaseInfo.objects.get(id=1)
    user.userextrainfo.username #扩展表名称需要小写

    result=UserExtraInfo.objects.get(id=1)
    result.user.username

def add_cardinfo(request):
    #获取用户基本表
    user=UserBaseInfo.objects.get(id=1)
    #添加卡信息表
    card=CardInfo(cardno='1111111111111111',bank='工商银行',user=user)
    card.save()
    card=CardInfo(cardno='2222222222222222222',bank='招商银行',user=user)
    card.save()

def query_cardinfo(request):
    #通过1查询多。获取用户基本表
    user=UserBaseInfo.objects.get(id=1)
    user.cardinfo_set.all()
    #通过多查询1
    card=CardInfo.objects.get(id=1)
    card.user.username

#多对多
def add_userskillinfo(request):
    #获取用户基本表
    user=UserBaseInfo.objects.all()
    #获取某个id=1的技能
    skill=SkillInfo.objects.get(id=1)
    #所有的用户增加id=1的技能
    result=skill.user.add(*user)



    d=dict(username="李四2",password='123456',status=1,
    createdate=timezone.now())
    userbaseinfo=UserBaseInfo.objects.create(**d)
    user=UserBaseInfo.objects.get(id=1)
    skill=SkillInfo.objects.get(id=1)
    result=skill.user.add(userbaseinfo)

def query_userskillinfo(request):
    #通过1查询多。获取用户基本表
    users=UserBaseInfo.objects.get(id=1)
    users.skillinfo_set.all()

    skills=SkillInfo.objects.all()
    for skill in skills:
        result=skill.user.all()
        print(result) 

def modify_userskillinfo(request):
    #获取用户基本表
    user=UserBaseInfo.objects.all()
    #获取某个id=1的技能
    skill=SkillInfo.objects.get(id=1)
    #修改全部用户的id=1的技能
    result=skill.user.set(user)
    #修改部分用户的id=1的技能
    user=[1,2]
    user=UserBaseInfo.objects.filter(status=1)
    result=skill.user.set(user)

def del_userskillinfo(request):
    #获取用户基本表
    user=UserBaseInfo.objects.get(id=1)
    #获取某个id=1的技能
    skill=SkillInfo.objects.get(id=1)
    #移除指定的用户
    result=skill.user.remove(user)
    result=skill.user.remove(2)
    result=skill.user.clear()

def sel_rel(request):
    cards=CardInfo.objects.all()
    for card in cards:
        print(card.user)
    cards=CardInfo.objects.select_related("user")
    for card in cards:
        print(card.user)

def pre_rel(request):
    skills=SkillInfo.objects.prefetch_related("user")
    for skill in skills:
        print(skill.skillname)
        users=skill.user.all()
        for user in users:
            print(user.username)
from django.db.models import F
def f_func(request):
    users=UserExtraInfo.objects.all()
    for user in users:
        user.salary+=1000
        user.save()
    
    for user in users:
        user.salary=F("salary")+1000
        user.save()
    

    #users.refresh_from_db()
    
    for user in users:
        user.refresh_from_db()
        print(user.salary)

from django.db.models import Q
def q_func(request):
    user=UserExtraInfo.objects.filter(Q(age__gt=30) & Q(salary__gt=5000))
    user

import json
def raw(request):
    users=UserExtraInfo.objects.raw("select * from userbaseinfo")
    for user in users:
        print(type(user),user)
    
    name="张三"
    sql='''
        select * from userextrainfo where username=%s
    '''
    users=UserExtraInfo.objects.raw(sql,[name])
    for user in users:
        print(user.id,user.username)
    
    sql='''select a.*,b.* from userbaseinfo a,userextrainfo b where a.id=b.user_id
    '''
    users=UserBaseInfo.objects.raw(sql)
    for user in users:
        print(user.age)

from django.db import connection
import django.utils.timezone as timezone
def cursor_insert(request):
    cursor=connection.cursor()
    insertsql="insert into departinfo(departname,createdate) values (%s,%s)"
    data=['总经办1',timezone.now()]
    cursor.execute(insertsql,data)#单条数据插入
    cursor.close()

def cursor_query(request):
    cursor=connection.cursor()
    cursor.execute("SELECT * from userextrainfo")
    row = cursor.fetchone() #获取某条数据
    print(row)
    cursor.close()

def cursor_update(request):
    cursor=connection.cursor()
    try:
        updatesql='update departinfo set departname=%s where id=%s'
        data=['销售部',2]
        cursor.execute(updatesql,data)
        rowcount=cursor.rowcount #影响的行数
        print(rowcount)
        connection.commit()
    except:
        connection.rollback()

def cursor_del(request):
    cursor=connection.cursor()
    sql="delete from departinfo where departname =%s"
    data=['总经办']
    cursor.execute(sql,data)#数据删除
    cursor.close()

from django.db import transaction
@transaction.atomic
def trans(request):
    #开启事务
    save_id=transaction.savepoint()
    try:
        #代码操作1
        #代码操作2
        transaction.savepoint_commit(save_id)
    except:
        transaction.savepoint_rollback(save_id)
    

def trans_with(request):
    with transaction.atomic():
        #开启事务
        save_id=transaction.savepoint()
        try:
            #代码操作1
            #代码操作2
            transaction.savepoint_commit(save_id)
        except:
            transaction.savepoint_rollback(save_id)

#@transaction.atomic
def userinfo_trans(request):
    #开启事务
    #save_id=transaction.savepoint()
    try:
        #基本信息保存
        d=dict(username="测试12",password='123456',status=1,
        createdate=timezone.now())
        userbaseinfo=UserBaseInfo.objects.create(**d)
        raise #抛出异常
        #扩展信息保存
        d=dict(username="测试12",truename='测试1',sex=0,salary=6555.88,age=35,
        status=0,createdate=timezone.now(),memo='',user=userbaseinfo)
        userextrainfo=UserExtraInfo.objects.create(**d)
        #transaction.savepoint_commit(save_id)
        msg="新增数据成功"
        print(msg)
    except:
        #transaction.savepoint_rollback(save_id)
        msg="新增数据失败"
        print(msg)
    return HttpResponse(msg)

def qs_all(request):
    users=UserExtraInfo.objects.all()
    print(users[0].truename)

def qs_filter(request):
    users=UserExtraInfo.objects.filter(sex=1)
    for user in users:
        print(user.truename)

def qs_exclude(request):
    users=UserExtraInfo.objects.exclude(age_lt=30)
    for user in users:
        print(user.truename)

def qs_distinct(request):
    users=UserExtraInfo.objects.distinct().values("department")
    print(users[0])

def qs_values(request):
    users=UserExtraInfo.objects.values()
    for user in users:
        print(type(user))
    users=UserExtraInfo.objects.values('id','username','truename')

def qs_query(request):
    users=UserExtraInfo.objects.all() #查询全部
    users=UserExtraInfo.objects.filter(id=10) #查询id=1的数据
    users=UserExtraInfo.objects.get(id=10) #查询id=1的数据

def qs_update(request):
    one_user=UserExtraInfo.objects.get(id=1)
    one_user.username='王五'
    one_user.save()
    one_user=UserExtraInfo.objects.filter(id=2).update(username='赵六')

    users=UserExtraInfo.objects.update(status=1)
    users2=UserExtraInfo.objects.filter(age__gt=35).update(salary=F('salary')+1000)

from django.db import connection,transaction
def query_sql(request):
    cursor=connection.cursor()
    cursor.execute("SELECT * from userextrainfo")
    row = cursor.fetchall()
    print(row)
    print(cursor.rowcount)
    cursor.close()

def query_insert(request):
    cursor=connection.cursor()
    insertsql="insert into departinfo(departname,createdate) values (%s,%s)"
    data=('总经办',timezone.now())
    cursor.execute(insertsql,data)#单条数据插入
    connection.commit()
    cursor.close()

from .forms import *
def testform(request):
    if request.method=="GET":
        myform=TestForm()
        return render(request,"5/testform.html",{'myform':myform})
    else:
        f=TestForm(request.POST)
        if f.is_valid():
            print(f["username"])
            print(f.cleaned_data["age"])
            return "ok"
        else:
            error=f.errors
            print(error)
            return render(request,"5/testform.html",locals())

# def userbaseinfoform(request):
    # if request.method=="GET":
    #     myform=UserBaseInfoForm()
    #     return render(request,"5/userbaseinfo.html",{'myform':myform})
    # else:
    #     f=UserBaseInfoForm(request.POST)
    #     if f.is_valid():
    #         print(f["username"])
    #         print(f.cleaned_data["age"])
    #         return "ok"
    #     else:
    #         error=f.errors
    #         print(error)
    #         return render(request,"5/userbaseinfo.html",locals())

def userinfo_set_form(request):
    if request.method=="GET":
        id=request.GET.get("id","")
        if id:
            UserBaseInfo.objects.filter(id=id)
            
        myform=UserBaseInfoForm()
        return render(request,"5/userbaseinfo.html",{'myform':myform})
    else:
        f=UserBaseInfoForm(request.POST)
        if f.is_valid():
            print(f["username"])
            print(f.cleaned_data["age"])
            return "ok"
        else:
            error=f.errors
            print(error)
            return render(request,"5/userbaseinfo.html",locals())

