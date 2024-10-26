from django.shortcuts import render
from .models import Patient
from .serializers import PatientSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def list_patients(request):
    patients = Patient.objects.all() # Query the database for all patients
    serializer = PatientSerializer(patients, many=True) # Serialize the patients
    return Response(Patient.objects.all()) # Return a response with all patients
