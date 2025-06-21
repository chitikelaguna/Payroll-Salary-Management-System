# Payroll-Salary-Management-System
# 🧾 Payroll & Salary Management System

A complete Payroll and Salary Management System built using **Django** and **MySQL**, with features like Employee Management, Attendance Tracking, Leave Applications, Salary Generation, and Admin Login Authentication.

---

## 🔧 Technologies Used

- Python 3.x  
- Django 4.x  
- MySQL  
- HTML5, CSS3, Bootstrap  
- Django Admin Panel  
- Django Authentication System  

---

## 📁 Features

✅ Admin Login / Logout  
✅ Dashboard Summary (Employees, Leaves, Salaries)  
✅ Employee CRUD (Add, Edit, Delete, View, Search)  
✅ Department & Designation Management  
✅ Attendance Management  
✅ Leave Management (Apply, Approve, Reject)  
✅ Salary Generation (Individual/Bulk) with Tax Calculation  
✅ Salary Status Update (Paid/Unpaid)

---

## 📂 Project Structure

payroll-management-system/
├── payroll_management_system/ # Main project folder
│ ├── init.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── payroll/ # Payroll app
│ ├── migrations/
│ │ └── init.py
│ ├── templates/
│ │ └── payroll/
│ │ ├── base.html
│ │ ├── login.html
│ │ ├── admin_dashboard.html
│ │ ├── employee_list.html
│ │ ├── add_employee.html
│ │ ├── edit_employee.html
│ │ ├── view_employee.html
│ │ ├── employee_search.html
│ │ ├── mark_attendance.html
│ │ ├── view_employee_attendance.html
│ │ ├── apply_leave.html
│ │ ├── leave_requests_list.html
│ │ ├── salary_detail.html
│ │ ├── add_department.html
│ │ ├── view_departments.html
│ │ ├── add_designation.html
│ │ └── view_designations.html
│ ├── static/
│ │ └── (optional CSS/JS files)
│ ├── admin.py
│ ├── apps.py
│ ├── forms.py
│ ├── models.py
│ ├── tests.py
│ ├── urls.py
│ └── views.py
│
├── db.sqlite3 or MySQL database (configured in settings)
├── manage.py
├── requirements.txt
└── README.md

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/chitikelaguna/payroll-management-system.git
cd payroll-management-system
