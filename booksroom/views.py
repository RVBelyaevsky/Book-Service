from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)

from booksroom.models import Books, Author, Booking
from booksroom.permissions import Moderator
from booksroom.serializers import BooksSerializer, AuthorSerializer, BookingSerializer

from rest_framework.permissions import AllowAny


class BooksListApiView(ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    permission_classes = [AllowAny]


class BooksRetrieveApiView(RetrieveAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


class BooksCreateApiView(CreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


class BooksDestroyApiView(DestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    permission_classes = [Moderator]


class BooksUpdateApiView(UpdateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    permission_classes = [Moderator]


class AuthorListApiView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorRetrieveApiView(RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorCreateApiView(CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDestroyApiView(DestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [Moderator]


class AuthorUpdateApiView(UpdateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [Moderator]


class BookingListApiView(ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class BookingCreateApiView(CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [Moderator]
