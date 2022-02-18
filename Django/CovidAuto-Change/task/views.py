from audioop import reverse
from django.shortcuts import redirect, render
from django.template import context
from .models import Task, Info
from django.contrib import auth
from django.contrib.auth.models import User

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
        pop_window_coordinate = request.POST.get('pop-window-coordinate', '')

        try:
            task = Task.objects.filter(id = int(task_id))[0]
            task.task_owner = request.user
            task.task_title = pop_window_title
            task.task_province = pop_window_province
            task.task_city = pop_window_city
            task.on_or_off = pop_window_on_or_off
            task.task_coordinate = pop_window_coordinate
            task.save()

            return redirect('/task/')
        except:
            return redirect('https://bilibili.com') # 出现无法创建task错误
    else: # 如果未登录，则跳转登录界面
        return redirect('/login_page/')

# 删除task方法
def delete_tasks(request):
    if request.user.username != '': # 如果登录成功
        task_id = request.POST.get('task-id', '') # 获取task_id
        try:
            task = Task.objects.filter(id = int(task_id))[0]
            task.delete()

            return redirect('/task/')
        except:
            return redirect('https://bilibili.com') # 出现无法删除task错误
    else: # 如果未登录，则跳转登录界面
        return redirect('/login_page/')

# 创建task方法
def create_tasks(request):
    if request.user.username != '': # 如果登录成功
        if request.POST.get('pop-window-on-or-off', 'False') == 'False':
            pop_window_on_or_off = False
        else:
            pop_window_on_or_off = True
        pop_window_title = request.POST.get('pop-window-title', '')
        pop_window_province = request.POST.get('pop-window-province', '')
        pop_window_city = request.POST.get('pop-window-city', '')
        pop_window_coordinate = request.POST.get('pop-window-coordinate', '')

        try:
            task = Task() # 新建task
            task.task_owner = request.user
            task.task_title = pop_window_title
            task.task_province = pop_window_province
            task.task_city = pop_window_city
            task.on_or_off = pop_window_on_or_off
            task.task_coordinate = pop_window_coordinate
            task.save()

            return redirect('/task/')
        except:
            return redirect('https://bilibili.com') # 出现无法创建task错误
    else: # 如果未登录，则跳转登录界面
        return redirect('/login_page/')

# information界面
def info_page(request):
    if request.user.username != '': # 如果登录成功

        try:
            context = {}
            info = Info.objects.filter(task_owner = request.user)
            if len(info) != 0: # 如果查询不成功，则新建
                info = Info.objects.filter(task_owner = request.user)[0]
                context['info'] = info
            else:
                info = Info()
                info.task_owner = request.user
                info.task_username = ''
                info.task_stu_id = ''
                info.task_phone = ''
                info.task_institution = ''
                info.task_form_id = ''
                info.vjuid = ''
                info.vjvd = ''
                info.vt = ''
                info.UUkey = ''
                info.save()
                # info = Info.objects.filter(task_owner = request.user)[0]
            # context['task_username'] = info.task_username
            # context['task_stu_id'] = info.task_stu_id
            # context['task_phone'] = info.task_phone
            # context['task_institution'] = info.task_institution
            # context['task_form_id'] = info.task_form_id
            # context['vjuid'] = info.vjuid
            # context['vjvd'] = info.vjvd
            # context['vt'] = info.vt
            # context['UUkey'] = info.UUkey
            

            return render(request, 'info.html', context)
        except:
            return redirect('https://bilibili.com') # 出现无法创建task错误
    else: # 如果未登录，则跳转登录界面
        return redirect('/login_page/')

# 修改info提交函数
def submit_info(request):
    if request.user.username != '': # 如果登录成功
        info_username = request.POST.get('info-username', '')
        info_password = request.POST.get('info-password', '')
        info_stu_id = request.POST.get('info-stu_id', '')
        info_phone = request.POST.get('info-phone', '')
        info_institution = request.POST.get('info-institution', '')
        info_form_id = request.POST.get('info-form_id', '')
        info_vjuid = request.POST.get('info-vjuid', '')
        info_vjvd = request.POST.get('info-vjvd', '')
        info_vt = request.POST.get('info-vt', '')
        info_UUkey = request.POST.get('info-UUkey', '')

        try:
            info = Info.objects.filter(task_owner = request.user)[0]
            info.task_username = info_username
            if info_password == '':
                user = User.objects.get(username = request.user.username)
            else:
                pass
            info.task_stu_id = info_stu_id
            info.task_phone = info_phone
            info.task_institution = info_institution
            info.task_form_id = info_form_id
            info.vjuid = info_vjuid
            info.vjvd = info_vjvd
            info.vt = info_vt
            info.UUkey = info_UUkey
            info.save()

            return redirect('/task/')
        except:
            return redirect('https://bilibili.com') # 出现无法创建task错误
    else: # 如果未登录，则跳转登录界面
        return redirect('/login_page/')