from django.contrib import admin
from .models import Task, Info

# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'task_owner', 'on_or_off', 'task_title', 'task_province', 'task_city')

@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'task_owner', 'task_username', 'task_stu_id', 'task_phone', 'task_institution', 'task_form_id', 'vjuid', 'vjvd', 'vt', 'UUkey')