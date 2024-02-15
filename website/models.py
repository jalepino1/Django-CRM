from django.db import models
import psycopg2



""" makemigrations → To update database models 
(We have to run this command every time when something changes in models.py e.g.
 adding a new table, changing a field name, etc"""


# Create your models here.
class Test(models.Model):
    Firstname = models.CharField(max_length=80)
    Lastname = models.IntegerField()
