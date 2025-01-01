class Book:
    def __init__(self, title, author, yearOfPublication):
        self.title = title
        self.author = author
        self.yearOfPublication = yearOfPublication

    def display(self):
        print(f'Title: {self.title}')
        print(f'Author: {self.author}')
        print(f'Price: {self.yearOfPublication}')

bookTitle=input("Enter your book details ('or done to finish')")

while(bookTitle.lower()!='done'):
    bookAuthor=input("Enter the Author Name")
    bookYearOfPublication=int(input("Enter the Year of Publication"))

    book1=Book(bookTitle,bookAuthor,bookYearOfPublication)
    book1.display()

    bookTitle = input("Enter your book details ('or done to finish')")