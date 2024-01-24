from django.test import TestCase
from django.urls import reverse

from .models import Book

class BookTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title = 'Test Title',
            subtitle = 'Test Subtitle',
            author = 'Test Author',
            isbn = '12345678890'
        )

    def test_book_content(self):

        self.assertEqual(self.book.title, 'Test Title')
        self.assertEqual(self.book.subtitle, 'Test Subtitle')
        self.assertEqual(self.book.author, 'Test Author')
        self.assertEqual(self.book.isbn, '12345678890')

    def test_book_listview(self):

        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Subtitle')
        self.assertTemplateUsed(response, "books/book_list.html")

    def test_str_return(self):

        self.assertEqual(self.book.__str__(), 'Test Title')
