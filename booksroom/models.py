from datetime import date
from django.db import models
from config import settings

NULLABLE = {"blank": True, "null": True}


class Author(models.Model):
    name = models.CharField(max_length=50, verbose_name="автор книги")
    country = models.CharField(max_length=100, verbose_name="страна автора", **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"


class Books(models.Model):
    GENRE = [
        ("Action", "Экшен"),
        ("Adventure", "Приключения"),
        ("Comedy", "Юмор"),
        ("Crime ", "Детективы"),
        ("Fantasy", "Фэнтэзи"),
        ("Historical", "Исторический"),
        ("Horror", "Ужасы"),
        ("Romance", "Любовные романы"),
        ("Satire ", "Сатира"),
        ("Science", "Научные"),
        ("Other", "Другое"),
    ]

    title = models.CharField(max_length=50, verbose_name="название книги")
    genre = models.CharField(
        max_length=50, choices=GENRE, verbose_name="жанр", default="Other"
    )
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, verbose_name="автор книги"
    )
    is_availability = models.BooleanField(
        verbose_name="наличие в библиотеке", default=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"


class Booking(models.Model):
    OPERATION = [("issuance", "выдача"), ("return", "возврат")]
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT, verbose_name="читатель"
    )
    book = models.ForeignKey(Books, on_delete=models.PROTECT, verbose_name="книга")
    operation = models.CharField(
        max_length=25, choices=OPERATION, verbose_name="действие", default="issuance"
    )
    booking_date = models.DateField(verbose_name="дата операции", default=date.today)

    def __str__(self):
        return f"Читатель {self.user} {self.operation} книгу {self.book}"

    class Meta:
        verbose_name = "действие над книгой"
        verbose_name_plural = "действия над книгами"
