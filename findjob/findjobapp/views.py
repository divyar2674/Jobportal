from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password,check_password
from findjobapp.models import Credentials
from findjobapp.models import Jobdata
from findjobapp.models import Jobseekerregistraion
from findjobapp.models import Applicants
from findjobapp.models import Employeeregisteration
# Create your views here.

@api_view(['POST'])
def signin(request):
    print("POST data:", request.data)
    username=request.data['username']
    oldpassword=request.data['password']
    password=make_password(oldpassword)
    role=request.data['role']
    print("role=",role)
    try:
     obj=Credentials(username=username,password=password,role=role)
     obj.save()
     if(role=="employer"):
       company=request.data['company']
       print("role=",company)
       email=request.data['email']
       about=request.data['about']
       emp=Employeeregisteration(empid=obj,company=company,email=email,about=about)
       emp.save()
       
     else:
       email=request.data.get("email")
       phonenumber=request.data.get("phonenumber")
       qualification=request.data.get("qualification")
       skills=request.data.get("skills")
       seek=Jobseekerregistraion(empid=obj,email=email,phonenumber=phonenumber,qualification=qualification,skills=skills)
       seek.save()
     return Response({'message':'pass'})
    except Exception as error:
       print("error occured" ,error)
       return Response({'message':'error'})
    

@api_view(['POST'])
def login(request):
     username=request.data.get('username')
     password=request.data.get('password')
     print("username",username)
     print("password",password)
     try:
        obj = Credentials.objects.get(username=username)
        if check_password(password, obj.password):
            return Response({'message': 'pass', "data":{'id':obj.id,'username':obj.username,'role': obj.role}})
        else:
            return Response({'message': 'failure'})  # wrong password
     except Credentials.DoesNotExist:
        return Response({'message': 'account does not exist please sign in'})
#add job in employer dashboard
@api_view(['POST'])
def add_job(request):
   print(request.data)
   try:
    userid=request.data.get('userid')
    emp=Credentials.objects.get(id=userid)
    empid=emp
    title=request.data.get('title')
    empcomp=Employeeregisteration.objects.get(empid=empid)
    company=empcomp.company
    location=request.data.get('location')
    job_type=request.data.get('job_type')
    duration=request.data.get('duration')
    mode=request.data.get('mode')
    salary=request.data.get('salary')
    skills=request.data.get('skills')
    lastdate=request.data.get('lastdate')
    
    obj=Jobdata(empid=empid,title=title,company=company,location=location,job_type=job_type,duration=duration,mode=mode,salary=salary,skills=skills,lastdate=lastdate,isfilled=False)
    obj.save()
    return Response({"message":"pass"})
   except Jobdata.DoesNotExist:
    return Response({"message":"error"})
#view only particular employer data(intial call)

@api_view(['POST'])
def viewjobs(request):
     jobid=request.data.get('id')
     obj=Jobdata.objects.filter(empid=jobid).values()
     if not obj:
        return Response({"message":"No data found "})
     return Response({"message":"pass","data":obj})

@api_view(['GET'])
def viewjobslist(request):
   obj=Jobdata.objects.all().order_by('posteddate').values()
   return Response({'message':'pass','data':obj})

@api_view(['POST'])
def delete(request):
   try:
     jobid=request.data.get('id')
     obj=Jobdata.objects.get(id=jobid)
     obj.delete()
     jobdata=Jobdata.objects.all().order_by('posteddate').values()
     return Response({'message':'success','data':jobdata})
   except Jobdata.DoesNotExist:
    return Response({"message":"data not found"})

#apply for jobs
@api_view(['POST'])
def applyjob(request):
   try:
      job=request.data.get("jobid")
      seeker=request.data.get("seekerid")
      jobid= Jobdata.objects.get(id=job)
      empid=jobid.empid
      print(Applicants._meta.get_fields())
      print("empid------->",empid)
      seekerid = Credentials.objects.get(id=seeker)
      status="pending"
      obj=Applicants(jobid=jobid,empid=empid,seekerid=seekerid,status=status)
      obj.save()
      
      return Response({"message":"pass","status":status,"seekerid":seekerid.id})
   except Exception as error:
      return Response({"message":str(error)})
   
@api_view(['POST'])
def edit(request):
   print(request.data)
   try:
      jobid=int(request.data.get("jobid"))
      empid=int(request.data.get("userid"))
      title=request.data.get('title')
      location=request.data.get('location')
      job_type=request.data.get('job_type')
      duration=request.data.get('duration')
      mode=request.data.get('mode')
      salary=request.data.get('salary')
      skills=request.data.get('skills')
      posteddate=request.data.get('posted_date')
      lastdate=request.data.get('lastdate')
      obj=Jobdata.objects.get(id=jobid,empid=empid)
      obj.title=title
      obj.company=obj.company
      obj.location=location
      obj.job_type=job_type
      obj.duration=duration
      obj.mode=mode
      obj.salary=salary
      obj.skills=skills
      obj.lastdate=lastdate
      obj.isfilled=False
      obj.save()
      return Response({"message":"pass"})
   except Jobdata.DoesNotExist:
      return Response({"message": "Invalid id"})

@api_view(['POST'])   
def editapplication(request): 
   try:  
       empid=int(request.data.get("empid"))
       username=request.data.get("username")
       email=request.data.get("email")
       phonenumber=request.data.get("number")
       qualification=request.data.get("qualification")
       skills=request.data.get("skills")
       user = Jobseekerregistraion.objects.get(empid=empid)
       user.username=username
       user.email=email
       user.phonenumber=phonenumber
       user. qualification=qualification
       user.skills=skills
       user.save()
       obj=Credentials.objects.get(id=empid)
       obj.username=username
       obj.save()
       return Response({"message":"pass"})
   except Jobseekerregistraion.DoesNotExist:
      return Response({"message": "Invalid id"})

@api_view(['POST'])
def getprofile(request):
   try:
      empid=int(request.data.get("empid"))
      user = Jobseekerregistraion.objects.filter(empid=empid).values()
      return Response({"message":"pass","data":user})
   except Jobseekerregistraion.DoesNotExist:
      return Response({"message":"fail"})

@api_view(['POST'])
def getapplicants(request):
   try:
    print("request--------->",request.data)
    empid=request.data.get("empid")
    emp=Credentials.objects.get(id=empid)
    obj=Applicants.objects.filter(empid=emp).values()
    seekerdata=[]
    finaldata=[]
    for i in obj:
       seekerid=i["seekerid_id"]
       data=Jobseekerregistraion.objects.filter(empid=seekerid).values().first()
       if(data):
          username=Credentials.objects.get(id=seekerid).username
          data['username']=username
       seekerdata.append(data)
       jobname=Jobdata.objects.get(id=i['jobid_id']).title
       print(jobname)
       finaldata.append({
          "jobid":i['jobid_id'],
          "jobname":jobname,
          "seekerinfo":data
       })
    print("seeker data->",finaldata)
    return Response({"message":"pass","data":finaldata})
   except Exception as error:
      return Response({"message":str(error)})
   
@api_view(['POST'])
def getempprofile(request):
   try:
      empid=int(request.data.get("empid"))
      user = Employeeregisteration.objects.filter(empid=empid).values()
      return Response({"message":"pass","data":user})
   except Employeeregisteration.DoesNotExist:
      return Response({"message":"fail"})
   
@api_view(['POST'])   
def editempprofile(request): 
   try:  
       empid=int(request.data.get("empid"))
       username=request.data.get("username")
       email=request.data.get("email")
       company=request.data.get("company")
       about=request.data.get('about')
       emp =Employeeregisteration.objects.get(empid=empid)
       emp.email=email
       emp.company=company
       emp.about=about
       emp.save()
       obj=Credentials.objects.get(id=empid)
       obj.username=username
       obj.save()
       return Response({"message":"pass"})
   except Employeeregisteration.DoesNotExist:
      return Response({"message": "Invalid id"})
