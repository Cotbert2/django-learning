from django.db import models
from patients.models import Patient
from doctors.models import Doctor

# Create your models here.

class Appoitment(models.Model):
    id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(
        Patient, related_name='appointments', on_delete=models.CASCADE)
    doctor = models.ForeignKey(
        Doctor, related_name='appointments', on_delete=models.CASCADE)
    
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=100)

class MedicalNote(models.Model):
    appoitment = models.ForeignKey(
        Appoitment, related_name='medical_notes', on_delete=models.CASCADE)
    note = models.TextField()
    date = models.DateField()