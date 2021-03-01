from .models import Task
from django.forms import ModelForm, TextInput, Textarea


class TaskForm (ModelForm):
	class Meta:
		model = Task
		fields = '__all__'
		widgets = {
		    "title": TextInput(attrs={
		    	'class': 'form-control',
		    	'placeholder': 'Enter Task Name'
			}),

			 "task": Textarea(attrs={
		    	'class': 'form-control',
		    	'placeholder': 'Enter Task Description'
			})
			 }