from django import forms
from .models import Employee

from django import forms

class EmployeeForm(forms.Form):
    # Dropdown for BusinessTravel
    BUSINESS_TRAVEL_CHOICES = [
        ('Some Travel', 'Some Travel'),
        ('No Travel', 'No Travel'),
        ('Frequent Traveller', 'Frequent Traveller'),
    ]
    
    # Dropdown for Department
    DEPARTMENT_CHOICES = [
        ('Sales', 'Sales'),
        ('Human Resources', 'Human Resources'),
        ('Technology', 'Technology'),
    ]
    
    # Dropdown for JobRole
    JOBROLE_CHOICES = [
        ('Sales Executive', 'Sales Executive'),
        ('HR Business Partner', 'HR Business Partner'),
        ('Engineering Manager', 'Engineering Manager'),
        ('Recruiter', 'Recruiter'),
        ('Data Scientist', 'Data Scientist'),
        ('Machine Learning Engineer', 'Machine Learning Engineer'),
        ('Manager', 'Manager'),
        ('Software Engineer', 'Software Engineer'),
        ('Senior Software Engineer', 'Senior Software Engineer'),
        ('Sales Representative', 'Sales Representative'),
        ('Analytics Manager', 'Analytics Manager'),
        ('HR Executive', 'HR Executive'),
        ('HR Manager', 'HR Manager'),
    ]
    
    # Dropdown for MaritalStatus
    MARITAL_STATUS_CHOICES = [
        ('Divorced', 'Divorced'),
        ('Single', 'Single'),
        ('Married', 'Married'),
    ]

    # Define form fields
    age = forms.IntegerField(label="Age")
    business_travel = forms.ChoiceField(choices=BUSINESS_TRAVEL_CHOICES, label="Business Travel")
    department = forms.ChoiceField(choices=DEPARTMENT_CHOICES, label="Department")
    job_role = forms.ChoiceField(choices=JOBROLE_CHOICES, label="Job Role")
    marital_status = forms.ChoiceField(choices=MARITAL_STATUS_CHOICES, label="Marital Status")
    salary = forms.IntegerField(label="Salary")
    overtime = forms.ChoiceField(choices=[('Yes', 'Yes'), ('No', 'No')], label="OverTime")
    years_at_company = forms.IntegerField(label="Years at Company")
    years_in_most_recent_role = forms.IntegerField(label="Years in Most Recent Role")
    years_since_last_promotion = forms.IntegerField(label="Years Since Last Promotion")

    class Meta:
        model = Employee
        feilds = "__all__"