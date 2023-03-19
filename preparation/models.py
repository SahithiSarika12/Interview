from django.db import models

# Create your models here.
class Register(models.Model):
	gender_val=[('male','male'),('female','female')]
	First_name=models.CharField(max_length=30)
	Last_name=models.CharField(max_length=30)
	Email=models.EmailField(max_length=50)
	Branch=models.CharField(max_length=10,default="")
	Gender=models.CharField(max_length=10,choices=gender_val)
	Date_of_birth=models.DateField(max_length=10)
	Password=models.CharField(max_length=30)
	Query=models.CharField(max_length=3000,default="")
	Answer=models.CharField(max_length=3000,default="")
	
class Adminlogin(models.Model):
	Username=models.CharField(max_length=30,primary_key=True)
	Password=models.CharField(max_length=30)
 
 #class Addquestion(models.Model):
	#question=models.CharField(max_length=4000)
	#answer=models.CharField(max_length=5000)

