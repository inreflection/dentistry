from django.db import models

class ServiceCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name='Категорія')
    description = models.TextField(verbose_name='Опис')
    photo = models.ImageField(upload_to='service_category_photos', verbose_name='Фото')

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=100, verbose_name='Послуга')
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, verbose_name='Категорія')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Ціна')

    def __str__(self):
        return self.name