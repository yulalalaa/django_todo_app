from django.shortcuts import render
from .models import Task
from .forms import TaskForm
from django.http import HttpResponse


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
			#return redirect ('home')

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
	return render (request, 'main/update.html')





