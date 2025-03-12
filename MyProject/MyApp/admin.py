from django.contrib import admin
from django.contrib.auth.models import User
from .models import Task, TaskGroup

# Register your models here.

class TaskGroupAdmin(admin.ModelAdmin):
	model = TaskGroup

	#optional modifications
	list_display = ('name',)
	list_filter = ('name',)

class TaskAdmin(admin.ModelAdmin):
	model = Task

	#optional modifications
	list_display = ('name', 'dateCreated',)

# class ProfileInline(admin.StackedInline):
# 	model = Profile
# 	can_delete = False

# class UserAdmin(admin.ModelAdmin):
# 	inlines = [ProfileInline]

admin.site.register(TaskGroup, TaskGroupAdmin)
admin.site.register(Task, TaskAdmin)

# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)