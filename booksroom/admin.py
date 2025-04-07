from django.contrib import admin

from booksroom.models import Author, Books, Booking


@admin.register(Author)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')


@admin.register(Books)
class UserAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Booking)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'operation', 'booking_date')
