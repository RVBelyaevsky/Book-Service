from django.contrib import admin

from booksroom.models import Author, Books, Booking


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "country")


@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("user", "book", "operation", "booking_date")
