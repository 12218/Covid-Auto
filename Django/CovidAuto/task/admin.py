from django.contrib import admin
from .models import Task

# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'task_owner', 'on_or_off', 'task_title', 'task_username', 'task_stu_id', 'task_phone', 'task_institution', 'task_province', 'task_city', 'task_form_id', 'vjuid', 'vjvd', 'vt', 'UUkey')
