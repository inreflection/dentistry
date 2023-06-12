from django.urls import path
from . import views

urlpatterns = [
    path('', views.allNews, name='allNews'),
    path('news/<int:pk>/', views.newsDetail, name='newsDetail'),
]
