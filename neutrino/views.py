from django.shortcuts import render
from doctors.models import DoctorModel

def home(request):
    doctors = DoctorModel.objects.all().order_by('-date_joined')
    return render(request, "index.html", {'doctors': doctors})