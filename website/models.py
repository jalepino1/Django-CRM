from django.db import models
import psycopg2



""" makemigrations → To update database models 
(We have to run this command every time when something changes in models.py e.g.
 adding a new table, changing a field name, etc"""


# Create your models here.
class Record(models.Model):
    # This will put a timestamp of whenever a record was added
    created_at = models.DateTimeField(auto_now_add=True)

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    zipcode = models.CharField(max_length=30)
    
    def __str__(self):
        return(f"{self.first_name} {self.last_name}")