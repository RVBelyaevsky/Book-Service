from rest_framework import status
from rest_framework.test import APITestCase


class BooksroomTestCase(APITestCase):
    def setUp(self):
        pass

    def test_list_book(self):
        """Тестирование вывода списка книг"""
        response = self.client.get("/booksroom/books/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
