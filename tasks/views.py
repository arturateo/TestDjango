from django.shortcuts import render
from django.template import loader

def index(request):
    return render(request, 'tasks/tasks_list.html', {})