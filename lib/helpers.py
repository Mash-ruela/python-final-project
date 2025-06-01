from models import session
from models.author import Author
from models.book import Book
from tabulate import tabulate

def list_authors():
    authors = session.query(Author).all()
    if authors:
        print(tabulate([[author.id, author.name] for author in authors], headers=['ID', 'Name'], tablefmt='grid'))
    else:
        print("No authors found.")

def add_author():
    name = input("Enter author name: ")
    if name:
        new_author = Author(name=name)
        session.add(new_author)
        session.commit()
        print(f"Author '{name}' added successfully.")
    else:
        print("Author name cannot be empty.")

def delete_author():
    list_authors()
    try:
        author_id = int(input("Enter author ID to delete: "))
        author = session.query(Author).get(author_id)
        if author:
            session.delete(author)
            session.commit()
            print(f"Author with ID {author_id} deleted successfully.")
        else:
            print(f"No author found with ID {author_id}.")
    except ValueError:
        print("Invalid input. Please enter a valid author ID.")

def add_book():
    title = input("Enter book title: ")
    year = input("Enter book year: ")
    list_authors()
    try:
        author_id = int(input("Enter author ID: "))
        book = Book(title=title, year=year, author_id=author_id)
        session.add(book)
        session.commit()
        print(f"Book '{title}' added successfully.")
    except ValueError:
        print("Invalid input. Please enter a valid author ID.")

def list_books():
    books = session.query(Book).all()
    if books:
        print(tabulate([[book.id, book.title, book.year, book.author.name] for book in books], headers=['ID', 'Title', 'Year', 'Author'], tablefmt='grid'))
    else:
        print("No books found.")

def delete_book():
    list_books()
    try:
        book_id = int(input("Enter book ID to delete: "))
        book = session.query(Book).get(book_id)
        if book:
            session.delete(book)
            session.commit()
            print(f"Book with ID {book_id} deleted successfully.")
        else:
            print(f"No book found with ID {book_id}.")
    except ValueError:
        print("Invalid input. Please enter a valid book ID.")

def exit_program():
    print("Exiting the program. Goodbye!")
    exit()