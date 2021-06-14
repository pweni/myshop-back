from django import forms
class UserInfoForm(forms.Form):
    '''用户状态'''
    STATUS=((0,'正常'), (1,'无效'),)
    username=forms.CharField(label="用户名",min_length=6)
    password=forms.CharField(label="密码",min_length=8,
    widget=forms.widgets.PasswordInput(attrs={"class":"password"},render_value=True)
    )
    status=forms.ChoiceField(label="用户状态",choices=STATUS,initial=1)
    createdate=forms.DateTimeField(label="创建时间")
    #age=forms.IntegerField(min_value=1,max_value=120,widget=forms.widgets.TextInput)
    #email=forms.EmailField(required=False,widget=forms.widgets.EmailInput)

class TestForm(forms.Form):
    '''用户状态'''
    STATUS=((0,'正常'), (1,'无效'),)
    username=forms.CharField(label="用户名",min_length=6)
    password=forms.CharField(label="密码",min_length=8,
    widget=forms.widgets.PasswordInput(attrs={"class":"password"},render_value=True)
    )
    status=forms.ChoiceField(label="用户状态",choices=STATUS,initial=1)
    createdate=forms.DateTimeField(label="创建时间")
    #age=forms.IntegerField(min_value=1,max_value=120,widget=forms.widgets.TextInput)
    #email=forms.EmailField(required=False,widget=forms.widgets.EmailInput)

from firstapp.models import *
class UserBaseInfoForm(forms.ModelForm):
    class Meta:
        #定义关联模型
        model=UserBaseInfo
        #定义需要在表单中展示的字段。
        fields=['username','password','status','createdate']
        #如果要显示全部字段，可以如下设置
        #fields="__all__"


    

