from django.shortcuts import render
from .models import Task


def index (request):
	tasks = Task.objects.all()
	return render (request, 'main/index.html', {'title': "Main Page", 'tasks': tasks})

def about (request):
	return render (request, 'main/about.html')
