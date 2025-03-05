from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Task, TaskGroup

@login_required
def home(request):
	# return HttpResponse("hello world")
	ctx = {
		'tasks':[
			"task1",
			"task2",
			"task3",
			"task4"
		]
	}
	return render(request, 'extendedTemplate.html', ctx)

def tasks(request):
	ctx = {
		'tasks':[
			"task1",
			"task2",
			"task3",
			"task4"
		]
	}
	return render(request, 'task_list.html', ctx)

def otherTasks(request, name=''):
	ctx = {
		'tasks':[
			"task1",
			"task2",
			"task3",
			"task4",
			name
		]
	}
	return render(request, 'task_list.html', ctx)

def basicParams(request, num=1):
	if num == 1:
		number = "first"
	elif num == 2:
		number = "second"
	else:
		number = "nth"
	return render(request, 'basicParams.html', {'number':number})

def basicTemplate(request):
	return render(request, 'basicParams.html')

def tasksInDatabase(request):
	#items = TaskGroup.objects.all()
	items = TaskGroup.objects.filter(name__contains="test")
	return render(request, 'task_list_objects.html', {'tasks': items})

def populateDatabase(request):
	TaskGroup.objects.create(name="createdTaskGroup", remarks="something happened")
	return render(request, 'task_list_objects.html')