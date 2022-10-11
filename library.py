class Library:
    def __init__(self,listOfBooks):
        self.books = listOfBooks

        
    def display(self):
        print("Books present in this library are: ")
        for book in self.books:
            
            print("\t" + book)
    def borrowBook(self,bookName):
        if bookName in self.books:
            print(f"You have issued {bookName} Please Keep it safe and return it within 30 Days")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry This book is not available Right Now")
            return False
    
    def returnBook(self,bookName):
        self.books.append(bookName)
        print("Thanks For returing this book Hope you enjoyed it")


class Student:
   def __init__(self):
       pass
   def requestBook(self):
    self.book = input("Enter the name of the book you want to borrow: ")
    return self.book

   def returnBook(self):
    self.book = input("Enter the name of the book you want to return: ")
    return self.book

if __name__ == "__main__":

 
   student = Student()
   centraLibrary = Library(["Algorithms", "Django", "Python Notes" ,"Clrs"])
   #centraLibrary.display()

   while(True):
    Welcomemsg = '''Welcome To Central Library
    Please choose an option:
    1. Listing all the books
    2. Request a book
    3. Add/Return a book
    4. Exit the Library'''
    
    print(Welcomemsg)
    
    a=int(input("Enter a choice: "))
    if a==1:
        centraLibrary.display()
    elif a==2:
        centraLibrary.borrowBook(student.requestBook())
    elif a==3:
        centraLibrary.returnBook(student.returnBook())
    elif a==4:
        print("Thanks For chossing Central Library")
        exit()
    else:
        print("Invalid choice")

   
