from django.db import models
from service.models import ServiceCategory, Service

class Appointment(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=12)
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
