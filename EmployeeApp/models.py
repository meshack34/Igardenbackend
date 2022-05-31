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
    Department = models.CharField(max_length=500)
    JobTitle = models.CharField(max_length=500)
    Requirements= models.CharField(max_length=500)
    NumberofDevelopers=models.CharField(max_length=250)
    DateOfApplication = models.DateField()
    FileName = models.CharField(max_length=500)

class Employees(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=500)
    LastName = models.CharField(max_length=500)
    PhoneNumber = models.CharField(max_length=250)
    Email = models.EmailField()
    Department = models.CharField(max_length=500)
    DateOfJoining = models.DateField()
    PhotoFileName = models.CharField(max_length=500)
    