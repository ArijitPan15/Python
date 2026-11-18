"""Interactive lending menu using Library and Book."""
from oop_library import Book, Library


def main(input_fn=input, output_fn=print):
    library = Library()
    while True:
        output_fn("1.Add 2.Borrow 3.Return 4.Available 5.Exit")
        choice = input_fn("Choice: ").strip()
        try:
            if choice == "1":
                library.add_book(Book(input_fn("ISBN: ").strip(), input_fn("Title: ").strip(), input_fn("Author: ").strip()))
                output_fn("Book added")
            elif choice == "2":
                output_fn(f"Borrowed: {library.borrow(input_fn('ISBN: ').strip()).title}")
            elif choice == "3":
                library.return_book(input_fn("ISBN: ").strip())
                output_fn("Book returned")
            elif choice == "4":
                for book in library.available_books():
                    output_fn(f"{book.isbn}: {book.title} by {book.author}")
            elif choice == "5":
                return
            else:
                output_fn("Invalid choice")
        except (ValueError, KeyError) as exc:
            output_fn(f"Error: {exc}")


if __name__ == "__main__":
    main()
