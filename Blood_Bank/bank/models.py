from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Userprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, null=True)
    contact = models.CharField(max_length=100, null=True)
    dob = models.DateField(null=True)
    address = models.CharField(max_length=100, null=True)
    blood_group = models.CharField(max_length=5, null=True)
    

    def __str__(self):
        return self.user.username


class Appointments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    name = models.CharField(max_length=20, null=True)
    email = models.EmailField(max_length=20, null=True)
    phone = models.CharField(max_length=15, null=True)
    date = models.DateField(null=True)
    reason = models.TextField(max_length=50, null=True)
    age = models.PositiveIntegerField(null=True)
    message = models.TextField()


    def __str__(self):
        return f"{self.name}'s Appointment"


