from django.shortcuts import render

from .models import Patient
from .serializers import PatientSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView

# Create your views here.
#Get api/patients/ 
#Post api/create-patients/
#Get api/patients/<pk>
#Put api/patients/<pk>


class ListPatientsView(ListAPIView, CreateAPIView):
    allowed_methods = ['GET', 'POST', 'HEAD', 'OPTIONS']
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()



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

