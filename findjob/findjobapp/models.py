from django.db import models
from datetime import date, timedelta
# Create your models here.


def get_due_date():
    return date.today()+timedelta(days=7)
class Credentials(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=50)
    role=models.CharField(max_length=15)

class Jobdata(models.Model):
    empid=models.ForeignKey(
        Credentials,on_delete=models.CASCADE,limit_choices_to={'role':'employee'}
    )
    title=models.CharField(max_length=100)
    company=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    job_type=models.CharField(max_length=50)
    duration=models.CharField(max_length=30)
    mode=models.CharField(max_length=10)
    salary=models.CharField(max_length=50)
    skills=models.CharField(max_length=200)
    posteddate=models.DateField(auto_now_add=True)
    lastdate=models.DateField(default=get_due_date)
    isfilled=models.BooleanField(default=False)

class Employeeregisteration(models.Model):
    empid=models.ForeignKey(Credentials,on_delete=models.CASCADE,null=True)
    company=models.CharField(max_length=100)
    email=models.EmailField()
    about=models.CharField(max_length=100)


class Jobseekerregistraion(models.Model):
    empid=models.ForeignKey(Credentials,on_delete=models.CASCADE,null=True)
    email=models.EmailField()
    phonenumber=models.CharField(max_length=15)
    qualification=models.TextField()
    skills=models.TextField()

class Applicants(models.Model):
    jobid=models.ForeignKey(Jobdata,on_delete=models.CASCADE,null=True)
    empid = models.ForeignKey(Credentials, on_delete=models.CASCADE, null=True,related_name="receiver")
    seekerid=models.ForeignKey(Credentials,on_delete=models.CASCADE,null=True,related_name="sender")
    status=models.TextField(default="pending",null=True)