class Book:

    def readBookDetails(self):
        self.__book_No = input("Enter bookno: ")
        self.__book_name = input("Enter book name: ")
        self.__Author = input("Enter author of book: ")
        self.__Publisher = input("Enter publisher of book: ")
        self.__Price = float(input("Enter price of book: "))
        self.__No_of_copies_issued = int(input("Enter number of copies: "))

    def displayBookDetails(self):
         print("Book number is " + str(self.__book_No))
         print("Book name is " + self.__book_name)
         print("Author is: " + self.__Author)
         print("Publisher is: " + self.__Publisher)
         print("Price is: " + str(self.__Price))
         print("No of copies issued: " + str(self.__No_of_copies_issued))

    def issueBook(self):
         self.__No_of_copies_issued = self.__No_of_copies_issued + 1

    def returnBook(self):
         self.__No_of_copies_issued = self.__No_of_copies_issued - 1


Book = Book()
Book.readBookDetails()
Book.issueBook()
Book.displayBookDetails()
Book.returnBook()
Book.displayBookDetails()