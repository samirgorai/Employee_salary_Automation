from django.db import models

# Create your models here.

class Employee(models.Model):
    employee_name=models.CharField(max_length=255)
    employee_ID=models.IntegerField()
    employee_joined_date=models.DateField()
    employee_monthly_salary=models.IntegerField()
    employee_adress=models.CharField(max_length=255)
    employee_designation=models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.employee_name
    
    