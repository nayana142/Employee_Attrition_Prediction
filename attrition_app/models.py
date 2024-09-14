from django.db import models

# Create your models here.
from django.db import models

# Create your Employee model
class Employee(models.Model):

    BUSINESS_TRAVEL_CHOICES = [
        ('Travel_Rarely', 'Travel_Rarely'),
        ('Travel_Frequently', 'Travel_Frequently'),
        ('Non-Travel', 'Non-Travel'),
    ]
    
    DEPARTMENT_CHOICES = [
        ('Sales', 'Sales'),
        ('Research & Development', 'Research & Development'),
        ('Human Resources', 'Human Resources'),
    ]
    
    JOB_ROLE_CHOICES = [
        ('Sales Executive', 'Sales Executive'),
        ('Manager', 'Manager'),
        ('Research Scientist', 'Research Scientist'),
        ('Research Director', 'Research Director'),
        ('Laboratory Technician', 'Laboratory Technician'),
        ('Human Resources', 'Human Resources'),
        ('Healthcare Representative', 'Healthcare Representative'),
        ('Sales Representative', 'Sales Representative'),
        ('Recruiter', 'Recruiter'),
    ]
    
    OVERTIME_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]
    
    MARITAL_STATUS_CHOICES = [
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Divorced', 'Divorced'),
    ]

    age = models.IntegerField()
    business_travel = models.CharField(max_length=20)
    department = models.CharField(max_length=30)
    job_role = models.CharField(max_length=50)
    marital_status = models.CharField(max_length=20)
    salary = models.FloatField()
    overtime = models.CharField(max_length=3)
    years_at_company = models.IntegerField()
    years_in_most_recent_role = models.IntegerField()
    years_since_last_promotion = models.IntegerField()

    def __str__(self):
        return f'{self.id} - {self.job_role}'

# Add any additional fields if necessary.
