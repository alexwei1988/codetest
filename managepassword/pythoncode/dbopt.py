import cx_Oracle

class Dbcon:
        name=''
	password=''
	connstr=''
	connection='';
	def __init__(self,username,password,connstr):
		self.name=username
		self.password=password
		self.connstr=connstr
		self.connection=self.getconn();
	def __del__(self):
		self.connection.close();

	def getconn(self):
		return cx_Oracle.connect(self.name,self.password,self.connstr)

	def changepassword(self,username,password):
		cursor=self.connection.cursor()
		cursor.callproc('change_password',[username,password])
		cursor.close()
		return "true" 

	def grant_role(self,username,rolename):
		cursor=self.connection.cursor()
		cursor.callproc('grant_roles',[username,rolename])
		cursor.close()
		return "true" 
		
		
        
