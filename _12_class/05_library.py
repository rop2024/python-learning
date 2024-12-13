# library Book Tracker: Make a Book class with attributes for title, author, and availability status.
# Add a method to change the status when the book is borrowed or returned.
# Then, create a Library class to manage a collection of Book objects.

class Book:
    def __init__(self, title,author, availability = True):
        self.title = title
        self.author = author
        self.availability = availability

    def __str__(self):
        if self.availability:
            avail = "available"
        else:
            avail = "not available"

        return f"{self.title} by {self.author} is {avail}"

    def availability_toggle(self):
        if self.availability:
            self.availability = False
        else:
            self.availability = True


class Library:

    def __init__(self):
        self.books = []

    def new_book(self):
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        newbook = Book(title, author)
        self.books.append(newbook)

        print("New book added!!")


    def remove_book(self):
        title = input("Enter the name of book that you want to delete: ")

        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print("Book was deleted !!")
                return

        print("No such book !!")


    def status_toggle(self, title):
        for book in self.books:
            if book.title == title:
                print(f"Current status : {book.availability}")
                book.availability_toggle()
                print(f"Status: {book.availability}")
                return

        print("No such book found !!")


    def search(self, title):
        for book in self.books:
            if book.title == title:
                print(f"Found !!")
                print(f"Availability : {book.availability}")
                return

        print("No book found !")

    def list(self):
        print("List of books -- ")
        print("| Name | Author | Availability |")
        for book in self.books:
            print(f"| {book.title} | {book.author} | {book.availability} |")

        print()
        print("End")


def main():
    xyz_library = Library()

    while True:
        print("----")
        print("1. Add new book")
        print("2. Remove book")
        print("3. Toggle book status")
        print("4. Search book")
        print("5. List book")
        print("6. Exit")

        choice = int(input("Enter choice(1-6): "))
        if 0 > choice > 7:
            print("Wrong choice  !!")
            break

        if choice == 1:
            xyz_library.new_book()

        elif choice == 2:
            xyz_library.remove_book()

        elif choice == 3:
            title = input("Enter name of book: ")

            xyz_library.status_toggle(title)

        elif choice == 4:
            title = input("Enter name of book: ")
            xyz_library.search(title)

        elif choice == 5:
            xyz_library.list()

        elif choice == 6:
            break

if __name__ == "__main__":
    main()