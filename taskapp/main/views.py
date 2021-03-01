from django.shortcuts import render
from .models import Task
from .forms import TaskForm
from django.http import HttpResponse
from django.http import HttpResponseRedirect


def index (request):
	tasks = Task.objects.order_by('-id')
	return render (request, 'main/index.html', {'title': "Main Page", 'tasks': tasks})

def about (request):
	return render (request, 'main/about.html')


def create (request):
	error = ''
	if request.method == 'POST':
		form = TaskForm (request.POST)
		if form.is_valid ():
			form.save ()
			return HttpResponseRedirect ('/')

		else:
			error = 'Not correct'

	form = TaskForm ()
	context = {
	    'form': form
	    #'error':error
	}
	return render (request, 'main/create.html', context)

def update (request, pk):
	el = Task.objects.get (id = pk)
	form = TaskForm (instance = el)
	if request.method == 'POST':
		form = TaskForm (request.POST, instance = el)
		if form.is_valid ():
			form.save ()
			return HttpResponseRedirect ('/')
	context = {
	    'form': form
	}
	return render (request, 'main/update.html', context)

def delete (request, pk):
	item = Task.objects.get (id = pk)
	if request.method == 'POST':
		item.delete ()
		return HttpResponseRedirect ('/')
	context = {
	    'item': item
	}
	return render (request, 'main/delete.html')






