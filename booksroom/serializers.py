from rest_framework.serializers import ModelSerializer

from booksroom.models import Books, Author, Booking


class BooksSerializer(ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
