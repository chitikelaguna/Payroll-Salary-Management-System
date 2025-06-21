from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100,null=False)
    def __str__(self):
        return self.name

class Designation(models.Model):
    title = models.CharField(max_length=100, null=False)
    def __str__(self):
        return self.title

class Employee(models.Model):
    emp_code = models.CharField(max_length=10, unique=True, null=False)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    dob = models.DateField()
    doj = models.DateField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    designation = models.ForeignKey(Designation,on_delete=models.CASCADE)
    basic_account = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Attendance(models.Model):
    status_choices = [
        ('Present','Present'),
        ('Absent','Absent'),
        ('Half','Half'),
    ]
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10,  )
    def __str__(self):
        return f"{self.employee.name} - {self.date} - {self.status}"

class Salary(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    month = models.IntegerField()
    year = models.IntegerField()
    basic_salary = models.DecimalField(max_digits=10, decimal_places=2)
    tax = models.DecimalField(max_digits=10, decimal_places=2)
    net_salary = models.DecimalField(max_digits=10, decimal_places=2)
    is_paid = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.employee.name} - {self.month}/{self.year}"

class Leave(models.Model):
    status_choices = [
        ("Pending", "Pending"),
        ("Approved", "Approved"),
        ("Rejected", "Rejected"),
    ]
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=10, choices=status_choices)
    def __str__(self):
        return f"{self.employee.name} - {self.leave_type} ({self.status})"