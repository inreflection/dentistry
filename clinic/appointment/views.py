from django.shortcuts import render, redirect
from .forms import AppointmentForm

def appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AppointmentForm()
    return render(request, 'appointment/appointment.html', {'form': form})
