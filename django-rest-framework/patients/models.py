from django.db import models

# Create your models here.

class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    contact_number = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    medical_history = models.TextField()

class MedicalRecord(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    diagnosis = models.TextField()
    treatment = models.TextField()
    date_of_next_visit = models.DateField()


class Insurance(models.Model):
    id = models.AutoField(primary_key=True)
    provider = models.CharField(max_length=100)
    policy_number = models.CharField(max_length=100)
    expiry_date = models.DateField()
