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
        return redirect('/')
    else:
        return redirect('https://bilibili.com')