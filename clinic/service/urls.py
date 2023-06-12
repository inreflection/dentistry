from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.categoryService, name='category'),
    path('category/<int:pk>/', views.category_detail, name='category_detail'),

]
