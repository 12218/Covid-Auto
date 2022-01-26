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
        return render(request, 'task.html', context)
    else: # 如果未登录，则跳转登录界面
        return redirect('/login_page/')

# 弹窗提交更改后信息
def submit_tasks(request):
    if request.user.username != '': # 如果登录成功
        if request.POST.get('pop-window-on-or-off', 'False') == 'False':
            pop_window_on_or_off = False
        else:
            pop_window_on_or_off = True
        task_id = request.POST.get('task-id', '') # 获取task_id
        pop_window_title = request.POST.get('pop-window-title', '')
        pop_window_province = request.POST.get('pop-window-province', '')
        pop_window_city = request.POST.get('pop-window-city', '')

        try:
            task = Task.objects.filter(id = int(task_id))[0]
            task.task_owner = request.user
            task.task_title = pop_window_title
            task.task_province = pop_window_province
            task.task_city = pop_window_city
            task.on_or_off = pop_window_on_or_off
            task.save()

            return redirect('/task/')
        except:
            return redirect('https://bilibili.com') # 出现无法创建task错误
    else: # 如果未登录，则跳转登录界面
        return redirect('/login_page/')