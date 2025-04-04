from django.contrib import admin

from booksroom.models import Author, Books


@admin.register(Author)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')


@admin.register(Books)
class UserAdmin(admin.ModelAdmin):
    list_display = ('title',)
