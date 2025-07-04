from django.contrib import admin
from findjobapp.models import Credentials
from findjobapp.models import Jobdata
from findjobapp.models import Jobseekerregistraion
from findjobapp.models import Applicants
from findjobapp.models import Employeeregisteration
# Register your models here.

admin.site.register(Credentials)
admin.site.register(Jobdata)
admin.site.register(Jobseekerregistraion)
admin.site.register(Applicants)
admin.site.register(Employeeregisteration)