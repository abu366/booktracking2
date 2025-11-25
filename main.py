import sys

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
    def info(self):
        return f"{self.book_id}: {self.title} by {self.author}"

class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        self.books.append(book)
    def show_books(self):
        for book in self.books:
            print(book.info())

def main(args):
    library = Library()

    if not args:
        print("Usage: add <id> <title> <author> | list")
        return

    cmd = args[0]

    if cmd == "add" and len(args) == 4:
        book = Book(args[1], args[2], args[3])
        library.add_book(book)
        print("Book added.")
    elif cmd == "list":
        library.show_books()
    else:
        print("Invalid command or arguments.")

if __name__ == "__main__":
    main(sys.argv[1:])
