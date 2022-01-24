from django.shortcuts import render
from django.template import context
from .models import Task

# Create your views here.
def login_page(request):
    context = {}
    return render(request, 'login.html', context)