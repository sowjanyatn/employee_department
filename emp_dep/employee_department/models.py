from django.db import models

# Create your models here.

class Department(models.Model):
    d_id = models.IntegerField(primary_key=True, null=False)
    d_name = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.d_name

class Employee(models.Model):
    e_id = models.IntegerField(primary_key=True, null=False)
    name = models.CharField(max_length=200, null=False)
    contact = models.IntegerField()
    salary = models.FloatField()
    role = models.CharField(max_length=200)
    # d_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name