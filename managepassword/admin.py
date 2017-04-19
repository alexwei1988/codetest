from django.contrib import admin
from .models import Manageruser,DbList,AllowedRoles

class ManagerUserAdmin(admin.ModelAdmin):
	        list_display=('uname','password','allowed_host',)

class DbListAdmin(admin.ModelAdmin):
	        list_display=('db_name','sid','connect_str',)

class AllowedRolesAdmin(admin.ModelAdmin):
	        list_display=('role_name',)	   

admin.site.register(Manageruser,ManagerUserAdmin)
admin.site.register(DbList,DbListAdmin)
admin.site.register(AllowedRoles,AllowedRolesAdmin)


# Register your models here.
