from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.dentistTeam, name='teamDentist'),
    path('doctor/<int:pk>/', views.doctor_detail, name='doctorDetail'),
]
