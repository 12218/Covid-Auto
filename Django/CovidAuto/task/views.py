from audioop import reverse
from django.shortcuts import redirect, render
from django.template import context
from .models import Task
from django.contrib import auth

# 登录页面
def login_page(request):
    context = {}
    return render(request, 'login.html', context)

# 登录函数
def login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    user = auth.authenticate(request, username = username, password = password) # 获取登录信息
    if user is not None:
        auth.login(request, user) # 登录
        return redirect('/task/')
    else:
        return redirect('https://bilibili.com')

# 控制台首页
def control_tasks(request):
    if request.user.username != '': # 如果登录成功
        context = {}
        context['tasks'] = Task.objects.filter(task_owner = request.user)
        return render(request, 'task_base.html', context)
    else: # 如果未登录，则跳转登录界面
        return redirect('/login_page/')