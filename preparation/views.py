
from django.shortcuts import render,redirect
from django.http import HttpResponse
from preparation.models import *
from interview import settings
from django.contrib import messages

# Create your views here.
def home(req):
	return render(req,"home.html")

def about(req):
	return render(req,"about.html")

def adminlogin(req):
	if req.method=='POST':
		uname=req.POST['username']
		pswd=req.POST['password']
		try:
			d=Adminlogin.objects.get(Username=uname,Password=pswd)
			if d.Password==pswd:
				#messages.success(req,"Login successfull")
				return render(req,'admin.html')
			else:
				return HttpResponse("Invalid password")
		except:
			messages.warning(req,"username not found")
	return render(req,'adminlogin.html')

def userlogin(req):
	if req.method=='POST':
		email=req.POST['email']
		pswd=req.POST['password']
		try:
			data=Register.objects.get(Email=email)
			if data.Password==pswd:
				#messages.success(req,"Login successfull")  
				return redirect("questionnaire")
			else:
				return HttpResponse("Invalid password")
		except:
			return HttpResponse("username not found")
	return render(req,"userlogin.html")

def register(req):
	if req.method=='POST':
		fnm=req.POST['First name']
		lnm=req.POST['Last name']
		email=req.POST['Email']
		branch=req.POST['Branch']
		gender=req.POST['Gender']
		dob=req.POST['Dob']
		pwd=req.POST['Pwd']
		data=Register.objects.create(First_name=fnm,Last_name=lnm,Email=email,Branch=branch,Gender=gender,Date_of_birth=dob,Password=pwd)
		data.save()
		# messages.success(req,"Your data added successfully") 
		return redirect("questionnaire")
	return render(req,'Signup.html')

def questionnaire(req):
	return render(req,"sidenav.html")

def query(req):
	if req.method=="POST":
		branch=req.POST['Branch']
		email=req.POST['TxtEmail']
		query=req.POST['textmsg']
		try:
			data=Register.objects.get(Email=email,Branch=branch) 
			Register.objects.filter(Email=email,Branch=branch).update(Query=query+data.Query)
			return HttpResponse("Your query successfully updated")
		except:
			return HttpResponse("Incorrect details")
	return render(req,"query.html")
 
def admin(req):
	return render(req,'admin.html')

def addadmin(req):
	if req.method=='POST':
		uname=req.POST['username']
		pswd=req.POST['password']
		try:
			Adminlogin.objects.create(Username=uname,Password=pswd)
			messages.success(req,"Data added successfully")
		except:
			messages.warning(req,"Incorrect data")
	return render(req,'addadmin.html')

def viewstudentquery(req):
	a=Register.objects.all()
	return render(req,'viewstudentquery.html',{"o":a})

def queryanswers(req):
	if req.method=='POST':
		branch=req.POST['Branch']
		mail=req.POST['Mail']
		answer=req.POST['Text']
		a=Register.objects.get(Email=mail,Branch=branch)
		Register.objects.filter(Email=mail,Branch=branch).update(Answer=answer+a.Answer)
		return HttpResponse("Answered successfully")
	return render(req,'queryanswers.html')


def email(req):
	if req.method=="POST":
		email=req.POST['Email']
		try:
			data=Register.objects.get(Email=email)
			if data is not None:
				return render(req,'answer.html',{"d":data})
		except:		
				#return HttpResponse("Invalid email")
				return render(req,"email.html")
	return render(req,'answer.html')

def answer(req):
	return render(req,'email.html')

def companycse(req):
	return render(req,'companycse.html')

def companyece(req):
	return render(req,'companyece.html')

def companyeee(req):
	return render(req,'companyeee.html')

def tcs(req):
	return render(req,'tcs.html')

def wipro(req):
	return render(req,'wipro.html')

def ibm(req):
	return render(req,'ibm.html')

def wiproece(req):
	return render(req,'wiproece.html')

def intel(req):
	return render(req,'intel.html')

def lg(req):
	return render(req,'lg.html')

def wiproeee(req):
	return render(req,'wiproeee.html')

def reliance(req):
	return render(req,'reliance.html')

def ongc(req):
	return render(req,'ongc.html')

#def addquestion(req):
	#if req.method=='POST':
		#ques=req.POST['textmsg']
		#ans=req.POST['answer']
	#return render(req,'addquestion.html')