from django.contrib import admin
from .models import Employee
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display=(
        'name_employee',
        'lastName1_employee',
        'lastName2_employee',
        'company_employee',
    )
admin.site.register(Employee,EmployeeAdmin)