from app5.models import *
from django import forms
from django.core.exceptions import ValidationError
import re


def mobile_validate(value):
    mobile_re = re.compile(
        r'^(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$')
    if not mobile_re.match(value):
        raise ValidationError('手机号码格式错误')


def age_validate(value):
    if value < 1 | value > 120:
        raise ValidationError('年龄范围为1-120岁')


class UserInfoForm(forms.Form):
    '''用户状态'''
    STATUS = ((None, '请选择'), (0, '正常'), (1, '无效'),)
    username = forms.CharField(label="用户名", min_length=6,
                               widget=forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': "请输入用户名"}))
    password = forms.CharField(label="密码", min_length=6, max_length=10,
                               widget=forms.widgets.PasswordInput(attrs={"class": "password"}, render_value=True))
    age = forms.IntegerField(label="年龄", initial=1)
    mobile = forms.CharField(label="手机号码")
    status = forms.ChoiceField(label="用户状态", choices=STATUS)
    # createdate=forms.DateTimeField(label="创建时间",required=False)


class UserBaseInfoForm(forms.Form):
    '''用户状态'''
    STATUS = ((None, '请选择'), (0, '正常'), (1, '无效'),)
    username = forms.CharField(label="用户名", min_length=6,
                               error_messages={
                                   'required': '用户姓名不能为空',
                                   'min_length': '长度最少6位',
                                   'invalid': '输入正确的用户姓名'
                               })
    age = forms.IntegerField(label="年龄", initial=1, validators=[age_validate],
                             error_messages={
        'required': '年龄不能为空',
    })
    status = forms.ChoiceField(label="用户状态", choices=STATUS,
                               error_messages={
                                   'required': '用户状态不能为空',
                               })
    createdate = forms.DateTimeField(label="创建时间", required=False)


class UserInfo_Msg_Form(forms.Form):
    '''用户状态'''
    STATUS = ((None, '请选择'), (0, '正常'), (1, '无效'),)
    username = forms.CharField(label="用户名", min_length=6,
                               widget=forms.widgets.TextInput(
                                   attrs={'class': 'form-control', 'placeholder': "请输入用户名"}),
                               error_messages={
                                   'required': '用户姓名不能为空',
                                   'min_length': '长度最少6位',
                                   'invalid': '输入正确的用户姓名'
                               })
    password = forms.CharField(label="密码", min_length=6, max_length=10,
                               widget=forms.widgets.PasswordInput(
                                   attrs={"class": "password"}, render_value=True),
                               error_messages={
                                   'max_length': '密码最长10位',
                                   'required': '密码不能为空',
                                   'min_length': '密码最少6位'
                               })
    age = forms.IntegerField(label="年龄", initial=1, validators=[age_validate],
                             error_messages={
        'required': '年龄不能为空',
    })
    mobile = forms.CharField(label="手机号码", validators=[mobile_validate],
                             error_messages={
        'required': '手机号码不能为空',
    })
    status = forms.ChoiceField(label="用户状态", choices=STATUS,
                               error_messages={
                                   'required': '用户状态不能为空',
                               })
    createdate = forms.DateTimeField(label="创建时间", required=False)


class WidgetForm(forms.Form):
    '''用户状态'''
    STATUS = ((None, '请选择'), (0, '正常'), (1, '无效'),)
    SKILL_STATUS = ((None, '请选择'), (0, '踢球'), (1, '音乐'), (2, '跑步'))
    username = forms.CharField(label="用户名", min_length=6,
                               widget=forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': "请输入用户名"}))
    password = forms.CharField(label="密码", min_length=6, max_length=10,
                               widget=forms.widgets.PasswordInput(attrs={"class": "password"}, render_value=True))
    age = forms.IntegerField(label="年龄", initial=1)
    status = forms.ChoiceField(
        label="用户状态", choices=STATUS, widget=forms.widgets.Select)
    skill = forms.ChoiceField(
        label="爱好", choices=SKILL_STATUS, widget=forms.widgets.SelectMultiple)


class TestForm(forms.Form):
    '''用户状态'''
    STATUS = ((0, '正常'), (1, '无效'),)
    username = forms.CharField(label="用户名", min_length=6)
    password = forms.CharField(label="密码", min_length=8,
                               widget=forms.widgets.PasswordInput(
                                   attrs={"class": "password"}, render_value=True)
                               )
    status = forms.ChoiceField(label="用户状态", choices=STATUS, initial=1)
    createdate = forms.DateTimeField(label="创建时间")
    # age=forms.IntegerField(min_value=1,max_value=120,widget=forms.widgets.TextInput)
    # email=forms.EmailField(required=False,widget=forms.widgets.EmailInput)


class UserBaseInfoModelForm(forms.ModelForm):
    confirm_password = forms.CharField(
        label='确认密码', widget=forms.PasswordInput(render_value=True),
        error_messages={
            'required': '密码不能为空',
        })

    class Meta:
        # 定义关联模型
        model = UserBaseInfo
        # 定义需要在表单中展示的字段。
        fields = ['username', 'password',
                  'confirm_password', 'age', 'mobile', 'status']
        # 如果要显示全部字段，可以如下设置
        # fields="__all__"
        # 如果Models中定义了名称，这里不用再定义
        labels = {
            "age": "最佳年龄",
            "mobile": "手机信息",
        }
        widgets = {
            # 文本框渲染为密码输入框
            "password": forms.widgets.PasswordInput(attrs={"class": "password"}, render_value=True)
        }
        error_messages = {
            "username": {
                'required': '用户姓名不能为空',
                'min_length': '长度最少6位',
                'invalid': '输入正确的用户姓名'
            },
            "password": {
                'max_length': '密码最长10位',
                'required': '密码不能为空',
                'min_length': '密码最少6位'
            },
            "age": {
                'required': '年龄不能为空',
            },
            "mobile": {
                'required': '手机号码不能为空',
            },
            "status": {
                'required': '用户状态不能为空',
            }
        }
    # 校验手机号码的局部钩子函数
    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')
        print(mobile)
        mobile_re = re.compile(r'^(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$')
        if not mobile_re.match(mobile):
            raise ValidationError('手机号码格式错误')
        return mobile

    # 全局钩子函数
    def clean(self):
        password =  self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("二次密码输入不一致")
