from django.shortcuts import render, redirect, get_object_or_404
from .models import Department,Designation,Attendance,Employee,Leave,Salary
from .forms import DesignationForm,DepartmentForm,AttendanceForm,EmployeeForm,LeaveForm,SalaryForm
from datetime import date
# Create your views here.

def admin_dashboard(request):
    context = {
        'employee_count':Employee.objects.count(),
        'leave_count':Leave.objects.count(),
        'salary_count':Salary.objects.count(),
    }
    return render(request,'payroll/admin_dashboard.html',context)

# Department Views 2

def add_department(request):
    form = DepartmentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('view_departments')
    return render(request,'payroll/add_department.html',{'form':form})

def view_departments(request):
    departments = Department.objects.all()
    return render(request,'payroll/view_departments.html',{'departments':departments})

# Designation Views 2

def add_designation(request):
    form = DesignationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('view_designations')
    return render(request, 'payroll/add_designation.html',{'form':form})

def view_designations(request):
    designations = Designation.objects.all()
    return render(request,'payroll/view_designations.html',{'designations':designations})

# Employee Views 6

def employee_list(request):
    employees = Employee.objects.all()
    return render(request,'payroll/employee_list.html',{'employees':employees})

def add_employee(request):
    form = EmployeeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("employee_list")
    return render(request,'payroll/add_employee.html',{'form':form})

def edit_employee(request,emp_id):
    employee = get_object_or_404(Employee, id=emp_id)
    form = EmployeeForm(request.POST or None, instance=employee)
    if form.is_valid():
        form.save()
        return redirect('employee_list')
    return render(request, 'payroll/edit_employee.html',{'form':form})

def delete_employee(request,emp_id):
    employee = get_object_or_404(Employee, id=emp_id)
    employee.delete()
    return redirect('employee_list')

def view_employee(request, emp_id):
    employee = get_object_or_404(Employee, id=emp_id)
    return render(request, 'payroll/view_employee.html',{'employee':employee})

def employee_search(request):
    query = request.GET.get('q')
    employees = Employee.objects.filter(name__icontains=query) if query else []
    return render(request,'payroll/employee_search.html',{'employees':employees})

# Attendance Views 3

def mark_attendance(request):
    form = AttendanceForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("attendance_report")
    return render(request, 'payroll/mark_attendance.html',{'form':form})

def attendance_report(request):
    attendances = Attendance.objects.all()
    return render(request, 'payroll/view_employee_attendance.html', {'attendances': attendances})


def view_employee_attendance(request, emp_id):
    employee = get_object_or_404(Employee, id=emp_id)
    records = Attendance.objects.filter(employee=employee)
    return render(request, 'payroll/view_employee_attendance.html',{'employee': employee, 'records': records})

# Salary Views 4

def generate_salary(request, emp_id):
    employee = get_object_or_404(Employee, id=emp_id)
    basic = float(employee.basic_account)
    tax = 0.05 * basic
    net = basic - tax
    Salary.objects.create(
        employee = employee,
        month = date.today().month,
        year =  date.today().year,
        basic_salary = basic,
        tax = tax,
        net_salary = net,
        is_paid = False
    )
    return redirect('view_salary_list')

def view_salary_list(request):
    salaries = Salary.objects.select_related('employee').all()
    return render(request, 'payroll/salary_detail.html',{'salaries':salaries})

def mark_salary_paid(request, salary_id):
    salary = get_object_or_404(Salary, id=salary_id)
    salary.is_paid = True
    salary.save()
    return redirect('view_salary_list')

def generate_bulk_salary(request):
    employees = Employee.objects.all()
    for employee in employees:
        basic = float(employee.basic_account)
        tax = 0.05 * basic
        net = basic - tax
        Salary.objects.create(
            employee=employee,
            month=date.today().month,
            year=date.today().year,
            basic_salary=basic,
            tax=tax,
            net_salary=net,
            is_paid=False
        )
    return redirect('view_salary_list')

# leave views 4

def apply_leave(request):
    form = LeaveForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('leave_requests_list')
    return render(request, 'payroll/apply_leave.html',{'form':form})

def leave_requests_list(request):
    leaves = Leave.objects.select_related('employee').all()
    return render(request, 'payroll/leave_requests_list.html',{'leaves':leaves})

def approve_leave(request, leave_id):
    leave = get_object_or_404(Leave, id=leave_id)
    leave.status = 'Approved'
    leave.save()
    return redirect('leave_requests_list')

def reject_leave(request, leave_id):
    leave = get_object_or_404(Leave, id=leave_id)
    leave.status='Rejected'
    leave.save()
    return redirect('leave_requests_list')