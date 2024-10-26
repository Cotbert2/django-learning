from django.db import models

# Create your models here.

class Doctor(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    biography = models.TextField()

class Department(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()

class DoctorAvailability(models.Model):
    id = models.AutoField(primary_key=True)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()



class MedicalNote(models.Model):
    id = models.AutoField(primary_key=True)
    note = models.TextField()
    date = models.DateField()