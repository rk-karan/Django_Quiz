from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    #this is kind of a flag
    is_student=models.BooleanField(default=False)
    is_teacher=models.BooleanField(default=False)

    #other features can also be added
    #first_name=models.CharField(max_length=100)
    #last_name=models.CharField(max_length=100)

class student(models.Model):
    #one to one fields is an instruction to the database saying there will be...
    #...only one user entry against one student entry.
    #on_delete=models.Cascade means than the student entry will be deleted when the user entry is deleted
    #for more information visit https://www.geeksforgeeks.org/python-relational-fields-in-django-models/
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

class teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
