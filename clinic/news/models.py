from django.db import models

class News(models.Model):
    title = models.CharField(max_length=100, verbose_name='Назва')
    photo = models.ImageField(upload_to='news_photos', verbose_name='Фото')
    content = models.TextField(verbose_name='Текст')
    publication_date = models.DateField(verbose_name='Дата публікації')

    def __str__(self):
        return self.title
