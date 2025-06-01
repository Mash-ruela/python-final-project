from models import session
from models.author import Author
from models.book import Book

def seed():
    # Seed authors
    authors = [
        Author(name='J.K. Rowling'),
        Author(name='George R.R. Martin'),
        Author(name='J.R.R. Tolkien')
    ]
    
    session.add_all(authors)
    session.commit()
    
    # Seed books
    books = [
        Book(title='Harry Potter and the Philosopher\'s Stone', year=1997, author_id=1),
        Book(title='A Game of Thrones', year=1996, author_id=2),
        Book(title='The Hobbit', year=1937, author_id=3)
    ]
    
    session.add_all(books)
    session.commit()
    
    print("Database seeded with initial data.")