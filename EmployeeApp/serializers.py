# //convent complex data to easy conversio to json

from rest_framework import serializers
from EmployeeApp.models import Departments,Employees, Recruiters, Developers, Bookspace

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Departments 
        fields=('DepartmentId','DepartmentName')


class RecruitSerializer(serializers.ModelSerializer):
    class Meta:
        model=Recruiters
        fields=('RecruiterId','CompanyName','PhoneNumber','Email','Department','JobTitle','Requirements','NumberofDevelopers','DateOfApplication','FileName')
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employees 
        fields=('EmployeeId','FirstName','LastName','PhoneNumber','Email','otherdetails','PhotoFileName')
class DevelopersSerializer(serializers.ModelSerializer):
    class Meta:
        model=Developers 
        fields=('HiredeveloperId','CompanyName','PhoneNumber','Email','JobTitle','Requirements','UploadFile')
        
class BookspaceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bookspace 
        fields=('BookspaceId','FirstName','LastName','PhoneNumber','Email','CompanyName','companySize','JobTitle','PreferredDate','PreferredTime','OtherDetails')
        