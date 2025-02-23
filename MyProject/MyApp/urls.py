from django.urls import path
from . import views

urlpatterns = [
	path("", views.home, name="home"),
	path("tasks/", views.tasks, name="tasks"),
	path("tasks/<str:name>/", views.otherTasks, name="otherTasks"),
	path("basicTemplate/", views.basicTemplate, name="basicTemplate"),
	path("basic/<int:num>/", views.basicParams, name="basicParams"),
	path("tasks/list/", views.tasksInDatabase, name="tasksInDatabase"),
	path("tasks/populate/", views.populateDatabase, name="populateDatabase"),
]