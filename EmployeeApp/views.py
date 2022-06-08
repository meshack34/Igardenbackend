
from django.shortcuts import render

# for other domain to access
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from EmployeeApp.models import Departments,Employees,Recruiters,Developers,Bookspace
from EmployeeApp.serializers import DepartmentSerializer,EmployeeSerializer, RecruitSerializer, DevelopersSerializer, BookspaceSerializer

from django.core.files.storage import default_storage

# Create your views here.

@csrf_exempt
def departmentApi(request,id=0):
    if request.method=='GET':
        departments = Departments.objects.all()
        departments_serializer=DepartmentSerializer(departments,many=True)
        return JsonResponse(departments_serializer.data,safe=False)
    elif request.method=='POST':
        department_data=JSONParser().parse(request)
        departments_serializer=DepartmentSerializer(data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        department_data=JSONParser().parse(request)
        department=Departments.objects.get(DepartmentId=department_data['DepartmentId'])
        departments_serializer=DepartmentSerializer(department,data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        department=Departments.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("Deleted Successfully",safe=False)
@csrf_exempt       
def hireApi(request,id=0):
    if request.method=='GET':
        hires = Developers.objects.all()
        hires_serializer=DevelopersSerializer(hires,many=True)
        return JsonResponse(hires_serializer.data,safe=False)
    elif request.method=='POST':
        hire_data=JSONParser().parse(request)
        hires_serializer=DevelopersSerializer(data=hire_data)
        if hires_serializer.is_valid():
            hires_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        hire_data=JSONParser().parse(request)
        hire=Developers.objects.get(HiredeveloperId=hire_data['HiredeveloperId'])
        hires_serializer=DevelopersSerializer(hire,data=hire_data)
        if hires_serializer.is_valid():
            hires_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        hire=Developers.objects.get(HiredeveloperId=id)
        hire.delete()
        return JsonResponse("Deleted Successfully",safe=False)
    
@csrf_exempt
def SavenewFile(request):
    file=request.FILES['UploadFile']
    file_name=default_storage.save(file.name,file)
    return JsonResponse(file_name,safe=True)

@csrf_exempt       
def bookspaceApi(request,id=0):
    if request.method=='GET':
        books = Bookspace.objects.all()
        books_serializer=BookspaceSerializer(books,many=True)
        return JsonResponse(books_serializer.data,safe=False)
    elif request.method=='POST':
        book_data=JSONParser().parse(request)
        books_serializer=BookspaceSerializer(data=book_data)
        if books_serializer.is_valid():
            books_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        book_data=JSONParser().parse(request)
        book=Bookspace.objects.get(BookspaceId=book_data['BookspaceId'])
        books_serializer=BookspaceSerializer(book,data=book_data)
        if books_serializer.is_valid():
            books_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        book=Bookspace.objects.get(BookspaceId=id)
        book.delete()
        return JsonResponse("Deleted Successfully",safe=False)
   
    
@csrf_exempt       
def recruitApi(request,id=0):
    if request.method=='GET':
        recruits = Recruiters.objects.all()
        recruits_serializer=RecruitSerializer(recruits,many=True)
        return JsonResponse(recruits_serializer.data,safe=False)
    elif request.method=='POST':
        recruit_data=JSONParser().parse(request)
        recruits_serializer=RecruitSerializer(data=recruit_data)
        if recruits_serializer.is_valid():
            recruits_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        recruit_data=JSONParser().parse(request)
        recruit=Recruiters.objects.get(RecruiterId=recruit_data['RecruiterId'])
        recruits_serializer=RecruitSerializer(recruit,data=recruit_data)
        if recruits_serializer.is_valid():
            recruits_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        recruit=Recruiters.objects.get(RecruiterId=id)
        recruit.delete()
        return JsonResponse("Deleted Successfully",safe=False)


@csrf_exempt
def employeeApi(request,id=0):
    if request.method=='GET':
        employees = Employees.objects.all()
        employees_serializer=EmployeeSerializer(employees,many=True)
        return JsonResponse(employees_serializer.data,safe=False)
    elif request.method=='POST':
        employee_data=JSONParser().parse(request)
        employees_serializer=EmployeeSerializer(data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        employee_data=JSONParser().parse(request)
        employee=Employees.objects.get(EmployeeId=employee_data['EmployeeId'])
        employees_serializer=EmployeeSerializer(employee,data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        employee=Employees.objects.get(EmployeeId=id)
        employee.delete()
        return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def SaveFile(request):
    file=request.FILES['file']
    file_name=default_storage.save(file.name,file)
    return JsonResponse(file_name,safe=False)