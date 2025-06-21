from django.contrib import admin
from .models import Department, Designation, Employee, Attendance, Salary, Leave
# Register your models here.

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Designation)
class DesignationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('emp_code','name','email','phone','department', 'designation')
    search_fields = ('emp_code','name','email')
    list_filter = ('department', 'designation')

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('employee', 'date', 'status')
    list_filter = ('status', 'date')
    search_fields = ('employee__name',)

@admin.register(Salary)
class SalaryAdmin(admin.ModelAdmin):
    list_display = ('employee','month','year','net_salary','is_paid')
    list_filter = ('month','year','is_paid')

@admin.register(Leave)
class LeaveAdmin(admin.ModelAdmin):
    list_display = ('employee','leave_type','start_date','end_date','status')
    list_filter = ('status','leave_type')
    