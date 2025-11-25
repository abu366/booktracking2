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

def main():
    library = Library()
    while True:
        print("1. Add book | 2. Show books | 3. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            b_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            book = Book(b_id, title, author)
            library.add_book(book)
        elif choice == "2":
            library.show_books()
        elif choice == "3":
            print("Bye!")
            break

if __name__ == "__main__":
    main()
