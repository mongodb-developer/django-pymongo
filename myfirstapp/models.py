from django.db import models

# Create your models here.
class Employee(models.Model):
	employee_id = models.CharField(max_length=20)
	employee_name = models.CharField(max_length=20)
	mobile_number = models.PositiveIntegerField()
	employee_title = models.CharField(max_length=10)
