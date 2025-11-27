from flask import Flask, request, render_template_string
import sys

# Copy your Book and Library classes from main.py
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
        return [book.info() for book in self.books]

app = Flask(__name__)
library = Library()  # Global library instance

HTML_TEMPLATE = """
<!doctype html>
<html>
<head>
    <title>Book Tracker Web App</title>
    <style>
        body { font-family: Arial; max-width: 800px; margin: 50px auto; }
        form { background: #f5f5f5; padding: 20px; border-radius: 8px; }
        input { margin: 5px; padding: 8px; width: 200px; }
        button { padding: 10px 20px; background: #007bff; color: white; border: none; border-radius: 4px; }
        ul { list-style: none; padding: 0; }
        li { background: #e9ecef; margin: 10px 0; padding: 15px; border-radius: 4px; }
    </style>
</head>
<body>
    <h1>📚 Book Tracker</h1>
    
    <form method="POST">
        <h3>Add New Book</h3>
        <input name="book_id" placeholder="Book ID" required><br>
        <input name="title" placeholder="Book Title" required><br>
        <input name="author" placeholder="Author Name" required><br>
        <button type="submit">Add Book</button>
    </form>

    <h3>📖 Current Books ({{ books|length }})</h3>
    {% if books %}
        <ul>
        {% for book in books %}
            <li>{{ book }}</li>
        {% endfor %}
        </ul>
    {% else %}
        <p>No books added yet.</p>
    {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        book_id = request.form['book_id']
        title = request.form['title']
        author = request.form['author']
        book = Book(book_id, title, author)
        library.add_book(book)
    
    books = library.show_books()
    return render_template_string(HTML_TEMPLATE, books=books)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
