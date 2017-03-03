from .models import DbList
from .models import AllowedRoles
from django import forms

class LoginForm(forms.Form):
	uname = forms.CharField(max_length=100,label="User name")
	pwd = forms.CharField(max_length=100,label="Password",widget=forms.PasswordInput)

class ChangePasswordForm(forms.Form):
	uname = forms.CharField(max_length=100,label="user name")
	newpwd= forms.CharField(max_length=100,label="password",widget=forms.PasswordInput)	
	dbname = forms.ModelChoiceField(queryset=DbList.objects.all(),label="Db name",to_field_name="connect_str")

class ChangeRoleForm(forms.Form):
	uname = forms.CharField(max_length=100,label="User name")
	rolename = forms.ModelChoiceField(queryset=AllowedRoles.objects.all(),label="avalible rows",to_field_name="role_name")
	dbname = forms.ModelChoiceField(queryset=DbList.objects.all(),label="Db name",to_field_name="connect_str")


class CreateUserForm(forms.Form):
	uname = forms.CharField(max_length=100,label="User name")
	newpwd= forms.CharField(max_length=100,label="password",widget=forms.PasswordInput)	
    dbname = forms.ModelChoiceField(queryset=DbList.objects.all(),label="Db name",to_field_name="connect_str")