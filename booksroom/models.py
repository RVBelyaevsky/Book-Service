from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Author(models.Model):
    name = models.CharField(max_length=50, verbose_name='автор книги')
    country = models.CharField(max_length=100, verbose_name='страна автора', **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"


class Books(models.Model):
    title = models.CharField(max_length=50, verbose_name='название книги')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
