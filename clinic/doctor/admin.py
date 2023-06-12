from django.contrib import admin
from .models import Specialization
from .models import Doctor

admin.site.register(Specialization)
admin.site.register(Doctor)