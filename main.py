import os

def main():
    ci_mode = os.getenv('CI', 'false').lower() == 'true'
    if ci_mode:
        print("Skipping interactive mode in CI")
        return

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
