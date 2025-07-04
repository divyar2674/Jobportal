from django.urls import path,include
from findjobapp import views as view

urlpatterns = [
    path('signin',view.signin,name="signin"),
    path('login',view.login,name="login"),
    path('add_job',view.add_job,name="add_job"),
    path('viewjobs',view.viewjobs,name="viewjobs"),
    path('viewjobslist',view.viewjobslist,name="viewjobslist"),
    path('delete',view.delete,name="delete"),
    path('applyjob',view.applyjob,name="applyjob"),
    path('edit',view.edit,name="edit"),
    path('editempprofile',view.editempprofile,name="editempprofile"),
    path('editapplication',view.editapplication,name="editapplication"),
    path('getprofile',view.getprofile,name="getprofile"),
    path('getempprofile',view.getempprofile,name="getempprofile"),
    path('getapplicants',view.getapplicants,name="getapplicants"),
    
]