from turtle import position
from django.db import models

# Create your models here.
class stuff(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    username = models.CharField(max_length=50)
    #title_postion = models.CharField(max_length=50)
    address= models.CharField(max_length=50)
