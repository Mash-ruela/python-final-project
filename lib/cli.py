from helpers import (list_authors, add_author, delete_author, list_books, add_book, delete_book, exit_program)

def main():
    while True:
        print("\nLibrary Management System")
        print("1. List Authors")
        print("2. Add Author")
        print("3. Delete Author")
        print("4. List Books")
        print("5. Add Book")
        print("6. Delete Book")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            list_authors()
        elif choice == '2':
            add_author()
        elif choice == '3':
            delete_author()
        elif choice == '4':
            list_books()
        elif choice == '5':
            add_book()
        elif choice == '6':
            delete_book()
        elif choice == '7':
            exit_program()
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    from models import Base, engine
    from models import author, book 
    Base.metadata.create_all(engine)  # Create tables if they don't exist
    main()