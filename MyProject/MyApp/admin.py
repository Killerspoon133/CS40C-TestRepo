from django.contrib import admin
from .models import Task, TaskGroup

# Register your models here.

class TaskGroupAdmin(admin.ModelAdmin):
	model = TaskGroup

	list_display = ('name',)
	list_filter = ('name',)

class TaskAdmin(admin.ModelAdmin):
	model = Task
	list_display = ('name', 'dateCreated',)

admin.site.register(TaskGroup, TaskGroupAdmin)
admin.site.register(Task, TaskAdmin)