#Defining a model

from django.db import models
class StudentModel(models.Model):
	name = models.charField(max_length = 50) 
	desc = model.textField()
	imag = models.DateTimeField()
	sec = models.imageField(upload_to='/tmp')

	def __str__(self):
		return self.name


python manage.py makemigrations
python manage.py migrate
from .models import StudentModel
from django.contrib import admin
admin.site.register(StudentModel)

#Inserting a model

student1 = StudentMdoel(name='anshu',,,)
student1.save()
Student.objects.all().values()#To see all the objects of StudentModel
StudentModel.object.all().values()

#Updating a model
from members.models import StudentModel
x = StudentModel.objects.all()[4]
x.name = 'sf'
x.save()

#Deleting a model
from members.models import StudentModel
x = StudentModel.objects.all()[2]
x.delete()

#Configuring database
In settings.py make sure that these settings are defined
DATABASE_ENGINE = ''#postgresql, postgresql_, sqlite3, oracle, mysql
DATABASE_NAME = ''
DATABASE_HOST = ''
DATABASE_PORT = ''
DATABASE_USERNAME = ''
DATABASE_PASSWORD = ''

from django.db import connection
cursor = connection.cursor()
