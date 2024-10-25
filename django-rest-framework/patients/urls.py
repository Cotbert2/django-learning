from django.urls import path
from patients.views import list_patients, create_patients, detail_patient


urlpatterns = [
    path('patients/', list_patients),
    path('create-patients/', create_patients),
    path('patients/<int:pk>', detail_patient),
]