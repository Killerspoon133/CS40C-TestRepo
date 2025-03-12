from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MyAccount

# Register your models here.
class MyAccountAdmin(UserAdmin):
	model = MyAccount
	list_display = ('email', 'username', 'is_staff', 'is_active')
	fieldsets = UserAdmin.fieldsets + (
		(None, {'fields':('phone_number',)}),
		)

	add_fieldsets = UserAdmin.add_fieldsets + (
		(None, {'fields':('email', 'phone_number',)}),
		)

admin.site.register(MyAccount, MyAccountAdmin)