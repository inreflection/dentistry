from django.db import models

class Specialization(models.Model):
    name = models.CharField(max_length=100, verbose_name='Спеціалізація')

    def __str__(self):
        return self.name


class Doctor(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Ім'я")
    last_name = models.CharField(max_length=100, verbose_name='Прізвище')
    specialization = models.ManyToManyField(Specialization, verbose_name='Спеціалізації')
    years_of_experience = models.IntegerField(verbose_name='Років досвіду роботи')
    education = models.CharField(max_length=100, verbose_name='Освіта')
    photo = models.ImageField(upload_to='doctor_photos', verbose_name='Фото')
    additional_info = models.TextField(verbose_name='Додаткова інформація про досвід роботи')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"