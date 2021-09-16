from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=200) # Varchar(200)
    email = models.CharField(max_length=200) # Varchar(200)
    department = models.CharField(max_length=100) # Varchar(100)
