from django.urls import path
from patients.views import   detail_patient, ListPatientsView



urlpatterns = [
    path('patients/', ListPatientsView.as_view()),
    path('patients/<int:pk>', detail_patient),
]