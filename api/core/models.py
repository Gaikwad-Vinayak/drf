from tkinter import CASCADE
from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=20)
    roll=models.IntegerField()
    city=models.CharField(max_length=20)

    # def __str__(self):
    #     return self.name
    

class teachers(models.Model):
    stu=models.ForeignKey(student,on_delete=models.CASCADE,related_name='stude')
    name=models.CharField(max_length=20)
    dept=models.CharField(max_length=20)

    # def __str__(self):
    #     return self.name
    
