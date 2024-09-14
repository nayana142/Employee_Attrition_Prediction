from django.contrib import admin

# Register your models here.
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'age', 'business_travel', 'department', 'job_role', 'salary', 'overtime')
    search_fields = ('job_role', 'department', 'marital_status')
    list_filter = ('business_travel', 'overtime', 'department')
