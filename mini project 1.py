# LIBRARY MANAGEMENT SYSTEM #
import sys
class Library:
    def __init__(self, books):
        self.books = books
    def dis_books(self):
        for book in self.books:
            print(book)
    def lend_book(self, a):
        print("Enter the name of the book you want to borrow : ")
        choice1 = input()
        if choice1 in self.books:
            self.books.remove(choice1)
            print(choice1, "has successfully been borrowed by you. ")
        else:
            print("Library does not contain this book.\n This book has been borrowed by",choice4)
    def add_book(self):
        print("Enter the book you want to add in this library : ")
        choice2 = input()
        self.books.append(choice2)
        print("Thanks for donating", choice2)
    def ret_book(self):
        print("Enter the name of the book you want to return : ")
        choice3 = input()
        self.books.append(choice3)
        print("Hello,",choice4,"You have successfully returned your book.")
if __name__ == '__main__':
    print("====WELCOME TO MY LIBRARY====")
    library = Library(["Python for beginners", "Learn C", "Java programming"])
    print("Please Enter Your Name:")
    choice4 = input()
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t WELCOME", choice4,", What would you like to do")
    lst = []
    lst.append(choice4)
    a = False
    while a == False:
        print("1>> Display available books\n"
              "2>> Lend a book\n"
              "3>> Add a book\n"
              "4>> Return a book\n"
              "5>> Exit"
              "6>> Number of customers visited")
        choice = int(input("Enter your choice : "))
        if choice == 1:
            print("Available books are : ")
            library.dis_books()
        elif choice == 2:
            print("Available books are : ")
            library.lend_book(library.dis_books())
        elif choice == 3:
            library.add_book()
        elif choice == 4:
            library.ret_book()
        else:
            print("Thanks for visiting")
            sys.exit()





