# Generated by Django 4.0.4 on 2022-06-07 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeApp', '0002_employees_otherdetails_alter_employees_dateofjoining_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employees',
            name='DateOfJoining',
        ),
    ]
