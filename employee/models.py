from django.db import models

# Create your models here.

class Employee(models.Model):
    employee_name=models.CharField(max_length=255)
    employee_ID=models.IntegerField(unique=True,primary_key=True)
    employee_joined_date=models.DateField()
    employee_monthly_salary=models.IntegerField()
    employee_adress=models.CharField(max_length=255)
    employee_designation=models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.employee_name
    


class Emp_salary(models.Model):
    #no_days_worked=models.IntegerField(models.ForeignKey)
    no_days_worked=models.IntegerField()
    employee_ID=models.ForeignKey(Employee,on_delete=models.CASCADE)
    total_working_days=models.IntegerField()

    def __str__(self) -> str:
        return str(self.no_days_worked)

