from django.db import models

# Create your models here.
class Todolist(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.BooleanField(default=False)
    date = models.DateField()
    

# Example model/database for notes app
class notes(models.Model):
    title = models.CharField(max_length=200)
    notes = models.TextField()
    date = models.DateField()
    

# Example model for practice
class students(models.Model):
    name = models.CharField(max_length=250)
    grade = models.CharField(max_length=250)
    hobby = models.TextField()

    

    
