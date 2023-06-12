from django.contrib import admin
from .models import Service
from .models import ServiceCategory

admin.site.register(Service)
admin.site.register(ServiceCategory)
