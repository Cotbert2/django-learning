from rest_framework import serializers

from .models import Appoitment, MedicalNote

class AppoitmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appoitment
        fields = '__all__'

class MedicalNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalNote
        fields = '__all__'