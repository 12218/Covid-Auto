from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    task_owner = models.ForeignKey(User, on_delete = models.DO_NOTHING) # 设置task使用者
    on_or_off = models.BooleanField(default = False) # 是否启用

    task_title = models.CharField(max_length = 50) # 任务名称
    task_username = models.CharField(max_length = 20) # 姓名
    task_stu_id = models.CharField(max_length = 20) # 学号
    task_phone = models.CharField(max_length = 20) # 电话号码
    task_institution = models.CharField(max_length = 20) # 学院
    task_province = models.CharField(max_length = 20) # 省份
    task_city = models.CharField(max_length = 30) # 城市
    task_form_id = models.CharField(max_length = 10) # 信息表中id

    vjuid = models.CharField(max_length = 20) # vjuid
    vjvd = models.CharField(max_length = 50) # vjvd
    vt = models.CharField(max_length = 20) # vt
    UUkey = models.CharField(max_length = 50) # UUkey
