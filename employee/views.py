from django.shortcuts import render
from employee.models import Employee,Emp_salary
from Additional_scripts import salary_calulator

# Create your views here.
def index(request):
    return render(request,'employee/index.html')

def query(request):
    return render(request,'employee/Query.html')


def employee_details(request):

    if(request.method =="GET"):
        #storing requersted from HTML page 
        requested_id=request.GET['employeeID']

        #requesting Employees data like name,salary,..
        em_obj=Employee.objects.get(employee_ID=requested_id)

        #requesting employees no of days worked
 
        em_salary_obj=Emp_salary.objects.get(employee_ID=requested_id)

        #calculate slary based on Total no of working days and no of days worked
        calulated_salary=salary_calulator.calculate_salary(em_salary_obj.total_working_days , em_salary_obj.no_days_worked , em_obj.employee_monthly_salary)

        #formating the data into a dictionary to send to html Employee details page
        dict_data_employee={'emp_name':em_obj.employee_name, 'emp_id':em_obj.employee_ID, 'twd':em_salary_obj.total_working_days, 'etwd':em_salary_obj.no_days_worked,'cal_sal':calulated_salary }

    return render(request,'employee/Employee_details.html',context=dict_data_employee)