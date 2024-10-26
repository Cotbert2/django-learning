from django.db import models
from patients.models import Patient
from doctors.models import Doctor

# Create your models here.

class Appoitment(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=100)

class MedicalNote(models.Model):
    id = models.AutoField(primary_key=True)
    note = models.TextField()
    date = models.DateField()