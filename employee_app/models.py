from django.db import models


class Employee(models.Model):
    emp_id = models.CharField(max_length=20)
    emp_name = models.CharField(max_length=50)
    desgination = models.CharField(max_length=50)
    department_name = models.CharField(max_length=50)

    def __str__(self): # by defining this str function means we tellling django thatyou are instructing Python on how to print the object. Now, anywhere that object is referenced—in the Django Admin,
        return self.emp_name
