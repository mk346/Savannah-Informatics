from django.contrib import admin
from .models import healthSys

# Register your models here.
@admin.register(healthSys)
# modifying the admin page
class myAdmin(admin.ModelAdmin):
	#modifying the table display 
	list_display = ('hName','county','system','sVersion')
	#ordering the table entries by name
	ordering =('hName',)
	#adding a search box into the admin page
	search_fields = ('hName','county','system')
	#filtering the fields using the given fields
	list_filter = ('system','sVersion')

