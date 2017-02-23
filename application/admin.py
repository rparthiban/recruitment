from django.contrib import admin

# Register your models here.
from .models import Application


class ApplicationAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['email', 'first_name']}),
        ('Information', {'fields': ['last_name', 'address',
        	'current_company', 'skills', 'active', 'accepted']}),
    ]
    list_display = ('email', 'first_name', 'last_name',
    	'current_company', 'skills', 'active', 'accepted')
    list_filter = ['active', 'skills']
    search_fields = ['email', 'first_name', 'current_company', 'skills']

admin.site.register(Application, ApplicationAdmin)
