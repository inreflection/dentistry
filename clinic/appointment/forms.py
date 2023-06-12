from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label=''
    )
    class Meta:
        model = Appointment
        fields = ['first_name', 'last_name', 'phone_number', 'category', 'date']
        labels = {
            'first_name': '',
            'last_name': '',
            'phone_number': '',
            'category': '',
            'date': ''
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': "Введіть ваше ім'я"}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Введіть ваше прізвище'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Введіть ваш номер телефону'}),
            'category': forms.Select(attrs={'placeholder': 'Оберіть послугу'}),
        }