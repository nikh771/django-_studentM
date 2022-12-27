from django.db import models

# Create your models here.
class STUDENT(models.Model):
    name=models.CharField(max_length=50)
    batch=models.IntegerField()
    department=models.CharField(max_length=50)
    mobile=models.IntegerField()
    rollno=models.IntegerField()