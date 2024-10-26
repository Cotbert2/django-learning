from django.shortcuts import render

from .models import Patient
from .serializers import PatientSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.

#Get api/patients/ 
#Post api/create-patients/
#Get api/patients/<pk>
#Put api/patients/<pk>

@api_view(['GET'])
def list_patients(request):
    print ('xd')
    print(Patient.objects.all())
    patients = Patient.objects.all() # Query the database for all patients
    serializer = PatientSerializer(patients, many=True) # Serialize the patients
    return Response(serializer.data) # Return a response with all patients


@api_view(['POST'])
def create_patients(request):
    serializer = PatientSerializer(data = request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'Delete'])
def detail_patient(request, pk):
    try:
        patient = Patient.objects.get(id=pk)
    except Patient.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PatientSerializer(patient)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = PatientSerializer(patient, data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    if request.method == 'DELETE':
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)