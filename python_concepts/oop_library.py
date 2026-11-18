"""Library inventory example demonstrating dataclasses and composition."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Book:
    isbn: str
    title: str
    author: str


class Library:
    def __init__(self):
        self._books = {}
        self._borrowed = set()

    def add_book(self, book):
        if not isinstance(book, Book):
            raise TypeError("expected Book")
        if book.isbn in self._books:
            raise ValueError("duplicate ISBN")
        self._books[book.isbn] = book

    def borrow(self, isbn):
        if isbn not in self._books:
            raise KeyError(isbn)
        if isbn in self._borrowed:
            raise ValueError("already borrowed")
        self._borrowed.add(isbn)
        return self._books[isbn]

    def return_book(self, isbn):
        if isbn not in self._borrowed:
            raise ValueError("book is not borrowed")
        self._borrowed.remove(isbn)

    def available_books(self):
        return [book for isbn, book in self._books.items() if isbn not in self._borrowed]
