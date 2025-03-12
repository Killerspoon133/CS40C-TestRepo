from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TaskGroup(models.Model):
	name = models.CharField(max_length=50)
	remarks = models.CharField(max_length=50, default="")
	otherRemarks = models.CharField(max_length=50, default="")

class Task(models.Model):
	name = models.CharField(max_length=200)
	isCompleted = models.BooleanField(default=False)
	isDelayed = models.BooleanField(default=False)
	dateCreated = models.DateTimeField(null=False)
	taskgroup = models.ForeignKey(TaskGroup, on_delete=models.CASCADE)

class MyNewTable(models.Model):
	custom_id = models.BigAutoField(primary_key=True)
	name = models.CharField(max_length=50)

# class Profile(models.Model):
# 	user = models.OneToOneField(User, on_delete=models.CASCADE)
# 	year_level = models.IntegerField()
# 	course = models.CharField(max_length=10)