# //convent complex data to easy conversio to json

from rest_framework import serializers
from EmployeeApp.models import Departments,Employees, Recruiters

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
        fields=('EmployeeId','FirstName','LastName','PhoneNumber','Email','Department','DateOfJoining','PhotoFileName')