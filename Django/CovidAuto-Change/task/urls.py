from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.control_tasks, name = 'control_tasks'),
]