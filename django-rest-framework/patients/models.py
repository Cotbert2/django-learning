from django.db import models

# Create your models here.

class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    contact_number = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    medical_history = models.TextField()

class MedicalRecord(models.Model):
    patient = models.ForeignKey(
        Patient, related_name='medical_records', on_delete=models.CASCADE)
    date = models.DateField()
    diagnosis = models.TextField()
    treatment = models.TextField()
    date_of_next_visit = models.DateField()


class Insurance(models.Model):
    patient = models.ForeignKey(
        Patient, related_name='insurance', on_delete=models.CASCADE)
    provider = models.CharField(max_length=100)
    policy_number = models.CharField(max_length=100)
    expiry_date = models.DateField()
