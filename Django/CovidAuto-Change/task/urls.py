from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.control_tasks, name = 'control_tasks'),
    path('submit_tasks/', views.submit_tasks, name = 'submit_tasks'),
    path('delete_tasks/', views.delete_tasks, name = 'delete_tasks'),
    path('create_tasks/', views.create_tasks, name = 'create_tasks'),
    path('info_page/', views.info_page, name = 'info_page'),
    path('submit_info/', views.submit_info, name = 'submit_info'),
]