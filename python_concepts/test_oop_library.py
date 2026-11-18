import unittest
from oop_library import Book, Library


class LibraryTests(unittest.TestCase):
    def test_lending(self):
        library = Library()
        book = Book("123", "Python", "Ada")
        library.add_book(book)
        self.assertEqual(library.available_books(), [book])
        self.assertEqual(library.borrow("123"), book)
        self.assertEqual(library.available_books(), [])
        library.return_book("123")
        self.assertEqual(library.available_books(), [book])

    def test_errors(self):
        library = Library()
        book = Book("123", "Python", "Ada")
        library.add_book(book)
        with self.assertRaises(ValueError):
            library.add_book(book)
        with self.assertRaises(KeyError):
            library.borrow("missing")
        library.borrow("123")
        with self.assertRaises(ValueError):
            library.borrow("123")


if __name__ == "__main__":
    unittest.main()
