# Generated by Django 4.0.4 on 2022-06-08 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeApp', '0004_developers_alter_employees_firstname_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookspace',
            fields=[
                ('BookspaceId', models.AutoField(primary_key=True, serialize=False)),
                ('FirstName', models.CharField(blank=True, max_length=500, null=True)),
                ('LastName', models.CharField(blank=True, max_length=500, null=True)),
                ('PhoneNumber', models.CharField(blank=True, max_length=250, null=True)),
                ('Email', models.EmailField(max_length=254)),
                ('CompanyName', models.CharField(blank=True, max_length=500, null=True)),
                ('JobTitle', models.CharField(blank=True, max_length=500, null=True)),
                ('companySize', models.CharField(blank=True, max_length=250, null=True)),
                ('PreferredDate', models.DateField()),
                ('PreferredTime', models.TimeField()),
                ('OtherDetails', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]