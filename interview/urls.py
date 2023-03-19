"""interview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from preparation import views 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('adminlogin/',views.adminlogin,name="adminlogin"),
    path('userlogin/',views.userlogin,name="userlogin"),
    path('home/',views.home,name="home"),
    path('register/',views.register,name="register"),
    path('about/',views.about,name="about"),
    path('tcs/',views.tcs,name="tcs"),
    path('wipro/',views.wipro,name="wipro"),
    path('ibm/',views.ibm,name="ibm"),
    path('wiproece/',views.wiproece,name="wiproece"),
    path('intel/',views.intel,name="intel"),
    path('lg/',views.lg,name="lg"),
    path('wiproeceee/',views.wiproeee,name="wiproeee"),
    path('reliance/',views.reliance,name="reliance"),
    path('ongc/',views.ongc,name="ongc"),
    path('questionnaire/',views.questionnaire,name="questionnaire"),
    path('query/',views.query,name="query"), 
    path('admin/',views.admin,name="admin"), 
    path('addadmin/',views.addadmin,name="addadmin"), 
    path('viewstudentquery/',views.viewstudentquery,name="viewstudentquery"), 
    path('queryanswers.html/',views.queryanswers,name="queryanswers"),
    path('answer.html/',views.answer,name="answer"),
    path('email.html/',views.email,name="email"),
    path('companycse.html/',views.companycse,name="companycse"),
    path('companyece.html/',views.companyece,name="companyece"),
    path('companyeee.html/',views.companyeee,name="companyeee"),
   # path('addquestion.html/',views.addquestion,name="addquestion"),
    ]
