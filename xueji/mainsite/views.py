from django.shortcuts import render
from mainsite import models
from mainsite import forms
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib.sessions.models import Session
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
# Create your views here.

def stu_add(request):                    # 处理从前端页面过来的请求
    if request.method=='POST':           # 如果是点击按钮提交
        stu_form=forms.StuForms(request.POST)   # 数据模型窗体实例化
        if stu_form.is_valid():           # 如果从页面提交的窗体数据是有效的
            message="你的信息已保存，谢谢！"
            stu_form.save()               # 把提交的数据保存到数据库
            return HttpResponseRedirect('/s_add')   # 前端转到list页面
        else:
            message="如果要添加学生，请每一个字段都填写。"
    else:
        stu_form=forms.StuForms()               # 前端页面刷新
        message = "如果要添加学生，请每一个字段都填写。"
    if request.user.is_authenticated:
        username=request.user.username
        messages.get_messages(request)
    return render(request,'stu_add.html',locals())    # 返回数据到前端页面进行渲染

def stu_list(request,bj):
    try:
       banji=models.Banji.objects.get(name=bj)
       student=models.Student.objects.filter(banji=banji)
    except:
        pass
    if 'username' in request.session:
        username=request.session['username']
        usercolor=request.session['usercolor']
    return render(request,'stu_list.html',locals())

def bj_list(request):
    nianji1=models.Nianji.objects.get(name='一年级')
    banji1=models.Banji.objects.filter(nianji=nianji1)
    nianji2 = models.Nianji.objects.get(name='二年级')
    banji2 = models.Banji.objects.filter(nianji=nianji2)
    nianji3 = models.Nianji.objects.get(name='三年级')
    banji3 = models.Banji.objects.filter(nianji=nianji3)
    nianji4 = models.Nianji.objects.get(name='四年级')
    banji4 = models.Banji.objects.filter(nianji=nianji4)
    nianji5 = models.Nianji.objects.get(name='五年级')
    banji5 = models.Banji.objects.filter(nianji=nianji5)
    nianji6 = models.Nianji.objects.get(name='六年级')
    banji6 = models.Banji.objects.filter(nianji=nianji6)
    if request.user.is_authenticated:
        username = request.user.username
        messages.get_messages(request)
    return render(request,'bj_list.html',locals())

def cj_add(request):
    teachers=models.Teacher.objects.all()
    students=models.Student.objects.all()
    try:
        user_s=request.GET['user_s']
        user_t=request.GET['user_t']
        user_yuwen=request.GET['user_yuwen']
        user_shuxue=request.GET['user_shuxue']
        user_yingyu=request.GET['user_yingyu']
        user_kexue=request.GET['user_kexue']
        user_yinyue=request.GET['user_yinyue']
        user_meishu=request.GET['user_meishu']
        user_tiyu=request.GET['user_tiyu']
        user_xinxi=request.GET['user_xinxi']
    except:
        user_s=None
        message='每一个字段都要填写。'

    if user_s!=None:
        student=models.Student.objects.get(name=user_s)
        teacher=models.Teacher.objects.get(name=user_t)
        chenji=models.Chengji.objects.create(student=student,teacher=teacher,yuwen=user_yuwen,shuxue=user_shuxue,yingyu=user_yingyu,kexue=user_kexue,yinyue=user_yinyue,meishu=user_meishu,tiyu=user_tiyu,xinxi=user_xinxi)
        chenji.save()
        message='成绩保存成功。'
    else:
        message = '每一个字段都要填写。'
    if request.user.is_authenticated:
        username = request.user.username
        messages.get_messages(request)
    return render(request,'cj_add.html',locals())

def cj_list(request,xs):
    try:
       student=models.Student.objects.get(name=xs)
       chengji=models.Chengji.objects.get(student=student)
    except:
       pass
    if request.user.is_authenticated:
        username = request.user.username
        messages.get_messages(request)
    return render(request,'cj_list.html',locals())

def login(request):
    if request.method=='POST':    # 检查进来的请求是否是“POST”
        login_form=forms.LoginForm(request.POST) # 如果是，实例化登录表单（POST)
        if login_form.is_valid():                # 如果表单的内容合理有效
            login_name=request.POST['username'].strip() # 提交的用户名赋值给login_name
            login_password=request.POST['password']     # 提交的密码赋值给login_password

            user=authenticate(username=login_name,password=login_password)  # 试着在系统自动的User表中进行验证
            if user is not None:              # 如果找到了
                if user.is_active:
                    auth.login(request,user)   # 将此用户存入session中
                    messages.add_message(request,messages.SUCCESS,'登录成功了')
                    return redirect('/')                       # 转向根目录网址
                else:
                    messages.add_message(request,messages.WARNING,'账号未启用')
            else:
                messages.add_message(request,messages.WARNING,'登录失败')   # 在User数据表中找不到用户
        else:
            messages.add_message(request,messages.INFO,'请检查输入的字段内容')
    else:
        login_form=forms.LoginForm()                       # 实例化非POST表单
    return render(request,'login.html',locals())           # 返回数值，渲染网页

def logout(request):                                      # 用户注销
    if 'username' in request.session:
        Session.objects.all().delete()
        return redirect('/login/')
    return redirect('/')

@login_required(login_url='/login/')
def userinfo(request):
    if request.user.is_authenticated:
        username=request.user.username
        try:
            user=User.objects.get(username=username)
            userinfo=models.Profile.objects.get(user=user)
        except:
            pass
    template=get_template('userinfo.html')
    html=template.render(locals())
    return HttpResponse(html)




