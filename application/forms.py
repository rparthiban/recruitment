from django import forms
from .models import Application

class ApplicationForm(forms.ModelForm):

	class Meta:
		model = Application
		fields = ('email', 'first_name', 'last_name', 'address', 'current_company', 'skills')
