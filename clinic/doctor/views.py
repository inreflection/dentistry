from django.shortcuts import render, get_object_or_404
from .models import Doctor

def doctor_detail(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    context = {'doctor': doctor}
    return render(request, 'doctor/doctor_detail.html', context)


def dentistTeam(request):
    doctors = Doctor.objects.all()
    context = {'doctors': doctors}
    return render(request, 'doctor/doctor.html', context)