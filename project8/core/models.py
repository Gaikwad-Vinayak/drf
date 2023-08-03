from django.db import models

# Create your models here.
class chat(models.Model):
    content=models.CharField(max_length=100)
    content2=models.IntegerField()