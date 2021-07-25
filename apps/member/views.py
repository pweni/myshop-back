from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from apps.member.models import *
from django.db.models import F

def add(request):
    return render(request,'shop/member/add.html')

def edit(request,id):
    print(id)
    return render(request,'shop/member/edit.html')

def delete(request,id):
    obj=Member.objects.get(member_id=id)
    obj.delete()
    json_dict={}
    json_dict["code"]=200
    json_dict["msg"]="删除数据成功"
    return JsonResponse(json_dict)

def index(request):
    if request.method=="GET":
        level=request.GET.get("level")
        truename=request.GET.get("truename",'')
        status=request.GET.get("status")

        search_dict=dict()
        if level:
            search_dict["level"]=level
        if truename: 
            search_dict["truename"]=truename
        if status:
            search_dict["status"]=status
        
        datas=Member.objects.filter(**search_dict).order_by("-member_id")

        page_size=2 #每页显示的行数
        try:
            if not request.GET.get("page"):
                curr_page=1
            curr_page=int(request.GET.get("page"))
        except:
            curr_page=1

        paginator=Paginator(datas,page_size)
        try:
            members=paginator.page(curr_page)
        except PageNotAnInteger:
            members=paginator.page(1)
        except EmptyPage:
            members=paginator.page(1)
        context={
            'level':level,
            'truename':truename,
            'status':status,
            'members':members,
        }
    return render(request,'shop/member/index.html',context=context)
#改进分页
def index_page(request):
    if request.method=="GET":
        page_size=100 #每页3条数据
        #page_size=int(request.GET["page_size"])
        try:
            if not request.GET["page"]:
                curr_page=1
            curr_page=int(request.GET["page"])
        except:
            curr_page=1
        #获取总数count
        total=Member.objects.count()
        #计算总页数
        total_page,remainder=divmod(total,page_size)
        if remainder:
            total_page+=1

        #通过切片获取当前页和下一页的数据
        members=Member.objects.order_by("-member_id")[(curr_page-1)*page_size:curr_page*page_size]
        return render(request,'member/index_page.html',{"members":members,"total_page":range(1,total_page+1),"curr_page":curr_page})
    
def get_memberinfo(request):
    if request.method=="GET":
        page_size=3
        curr_page=int(request.GET["page"])
        #获取总数count
        total=models.member.objects.count()
        #通过切片获取当前页和下一页的数据
        members=models.member.objects.order_by("-id")[(page_num-1)*page_size:page_num*page_size]
        rows=[]
        datas={"total":total,"rows":rows}
        for member in members:
            rows.append({
                "id":member.member_id,
                "username":member.username,
                "truename":member.treuname,
            })
        return HttpResponse(json.dumps(datas),content_type="application/json")


def list(request):
    return render(request,'member/list.html')

def index_bttable(request):
    return render(request,'shop/member/index_bttable.html')

def ajax_member(request):
    total=Member.objects.count()
    members=Member.objects.order_by("-member_id")
    rows=[]
    datas={"total":total,"rows":rows}
    for member in members:
        rows.append({
            "id":member.member_id,
            "username":member.username,
            "truename":member.truename,
            "sex":member.sex,
            "email":member.email,
            })
    return JsonResponse(datas,safe=False,json_dumps_params={'ensure_ascii':False,"indent":4})
