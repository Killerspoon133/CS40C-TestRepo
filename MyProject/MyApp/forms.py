from django import forms
from .models import TaskGroup

class TaskGroupForm(forms.ModelForm):
	class Meta:
		model = TaskGroup
		fields = '__all__'
		# This is equivalent to:
		# fields = ['name', 'remarks', 'otherRemarks']

class TaskGroupOtherForm(forms.Form):
	name = forms.CharField(max_length=10, required=True)
	remarks = forms.CharField(widget=forms.Textarea)