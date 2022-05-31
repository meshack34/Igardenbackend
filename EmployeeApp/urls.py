from django.urls import re_path
from EmployeeApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    re_path(r'^department$',views.departmentApi),
    re_path(r'^department/([0-9]+)$',views.departmentApi),

    re_path(r'^employee$',views.employeeApi),
    re_path(r'^employee/([0-9]+)$',views.employeeApi),
    re_path(r'^employee/savefile',views.SaveFile),
    
    re_path(r'^recruiter$',views.recruitApi),
    re_path(r'^recruiter/([0-9]+)$',views.recruitApi),
    re_path(r'^recruiter/savefile',views.SaveFile)
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)