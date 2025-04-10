from django.urls import path

from booksroom.apps import BooksroomConfig

from booksroom.views import (
    BooksListApiView,
    BooksRetrieveApiView,
    BooksCreateApiView,
    BooksDestroyApiView,
    BooksUpdateApiView,
    AuthorListApiView,
    AuthorRetrieveApiView,
    AuthorDestroyApiView,
    AuthorCreateApiView,
    AuthorUpdateApiView,
    BookingListApiView,
    BookingCreateApiView,
)

app_name = BooksroomConfig.name


urlpatterns = [
    path("books/", BooksListApiView.as_view(), name="books_list"),
    path("books/<int:pk>/", BooksRetrieveApiView.as_view(), name="books_retrieve"),
    path("books/create/", BooksCreateApiView.as_view(), name="books_create"),
    path("books/<int:pk>/delete/", BooksDestroyApiView.as_view(), name="books_delete"),
    path("books/<int:pk>/update/", BooksUpdateApiView.as_view(), name="books_update"),
    path("author/", AuthorListApiView.as_view(), name="author_list"),
    path("author/<int:pk>/", AuthorRetrieveApiView.as_view(), name="author_retrieve"),
    path("author/create/", AuthorCreateApiView.as_view(), name="author_create"),
    path(
        "author/<int:pk>/delete/", AuthorDestroyApiView.as_view(), name="author_delete"
    ),
    path(
        "author/<int:pk>/update/", AuthorUpdateApiView.as_view(), name="author_update"
    ),
    path("booking/", BookingListApiView.as_view(), name="booking_list"),
    path("booking/create/", BookingCreateApiView.as_view(), name="booking_create"),
]
