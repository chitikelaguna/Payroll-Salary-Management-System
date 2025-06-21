from django import forms
from .models import Department,Designation,Employee,Attendance,Salary,Leave

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name']

class DesignationForm(forms.ModelForm):
    class Meta:
        model = Designation
        fields = ['title']

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            'emp_code', 'name', 'email','phone',
            'dob','doj','department','designation','basic_account'
        ]

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['employee', 'date', 'status']

class SalaryForm(forms.ModelForm):
    class Meta:
        model = Salary
        fields = [
            'employee', 'month', 'year',
            'basic_salary','tax','net_salary','is_paid'
        ]

class LeaveForm(forms.ModelForm):
    class Meta:
        model = Leave
        fields = [
            'employee','leave_type','start_date','end_date','status'
        ]
