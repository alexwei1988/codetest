from django.contrib import admin
from .models import Manageruser,DbList

class ManagerUserAdmin(admin.ModelAdmin):
	        list_display=('uname','password','allowed_host',)

class DbListAdmin(admin.ModelAdmin):
	        list_display=('db_name','sid','connect_str',)

admin.site.register(Manageruser,ManagerUserAdmin)
admin.site.register(DbList,DbListAdmin)

# Register your models here.
