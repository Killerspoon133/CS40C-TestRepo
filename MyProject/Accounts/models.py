from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class MyAccount(AbstractUser):
	# unique email means in our db, you will not see duplicate emails in accounts
	email = models.EmailField(unique=True)
	phone_number = models.CharField(max_length=15, blank=True, null=True)

	# use the 'email' field for authentication
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']

	def __str__(self):
		return f"Account username is: {self.email}"