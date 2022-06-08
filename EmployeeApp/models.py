from django.db import models

# Create your models here.

class Departments(models.Model):
    DepartmentId = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=500)
    
class Recruiters(models.Model):
    RecruiterId = models.AutoField(primary_key=True)
    CompanyName = models.CharField(max_length=500)
    PhoneNumber = models.CharField(max_length=250)
    Email = models.EmailField()
    Department = models.CharField(max_length=500, null=True,blank = True)
    JobTitle = models.CharField(max_length=500)
    Requirements= models.CharField(max_length=500)
    NumberofDevelopers=models.CharField(max_length=250)
    DateOfApplication = models.DateField()
    FileName = models.CharField(max_length=500)

class Employees(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=500, null=True,blank = True)
    LastName = models.CharField(max_length=500 , null=True,blank = True)
    PhoneNumber = models.CharField(max_length=250, null=True,blank = True)
    Email = models.EmailField()
    otherdetails = models.CharField(max_length=250, null=True,blank = True)
    # DateOfJoining = models.DateField(null=True,blank = True)
    PhotoFileName = models.CharField(max_length=500, null=True,blank = True)
    
class Developers(models.Model):
    HiredeveloperId = models.AutoField(primary_key=True)
    CompanyName = models.CharField(max_length=500, null=True,blank = True)
    PhoneNumber = models.CharField(max_length=250, null=True,blank = True)
    Email = models.EmailField()
    JobTitle = models.CharField(max_length=500 , null=True,blank = True)
    Requirements = models.CharField(max_length=250, null=True,blank = True)
    UploadFile = models.CharField(max_length=500, null=True,blank = True)

class Bookspace(models.Model):
    BookspaceId = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=500, null=True,blank = True)
    LastName = models.CharField(max_length=500 , null=True,blank = True)
    PhoneNumber = models.CharField(max_length=250, null=True,blank = True)
    Email = models.EmailField()
    CompanyName = models.CharField(max_length=500, null=True,blank = True)
    JobTitle = models.CharField(max_length=500 , null=True,blank = True)
    companySize = models.CharField(max_length=250, null=True,blank = True)
    PreferredDate = models.DateField()
    PreferredTime =models.TimeField(null=True,blank = True)
    OtherDetails = models.CharField(max_length=500, null=True,blank = True)   

    
    