from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from .models import Task, TaskGroup
from .forms import TaskGroupForm, TaskGroupOtherForm

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

def populateDatabase(request):
	TaskGroup.objects.create(name="createdTaskGroup", remarks="something happened")
	return render(request, 'task_list_objects.html')

def oldTasksInDatabase(request):

	if (request.method == "POST"):
		taskgroup = TaskGroup()
		taskgroup.name = request.POST.get('task_name')
		taskgroup.save()
		items = TaskGroup.objects.all()
		ctx = {"taskgroups":items}

		return render(request, 'task_list_objects.html', ctx)

	items = TaskGroup.objects.all()
	ctx = {"taskgroups":items}
	print(f"request type: {request.method}")
	print(f"ctx: {ctx}")

	return render(request, 'MyApp/task_group_list.html', {'tasks': items})

def tasksInDatabase(request):

	if (request.method == "POST"):
		form = TaskGroupForm(request.POST, request.FILES)

		if form.is_valid():
			form.save() # <-- for forms.ModelForm stuff
			# TaskGroup.objects.create(
			# 	name=form.cleaned_data['name'],
			# 	remarks=form.cleaned_data['remarks']
			# )

			return redirect('tasksInDatabase')

	form = TaskGroupForm()
	items = TaskGroup.objects.all()
	ctx = {"taskgroups":items}

	print(f"request type: {request.method}")
	print(f"ctx: {ctx}")

	return render(request, 'MyApp/task_group_list.html', {'tasks': items, 'task_form':form})
