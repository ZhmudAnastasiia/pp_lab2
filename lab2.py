class Book:
    
    def __init__(self, title, author_name, published_year, location=None):
        self.__title = title
        self.__author = author_name
        self.published_year = published_year
        self.location = location
    
    def title(self):
        return self.__title
    
    def author(self):
        return self.__author
    
    def get_info(self):
        return f'Title: {self.title()}, Author: {self.author()}, Published in: {self.published_year}, Location: {self.location}'

    def set_location(self, shelf, section):
        self.location = {'section': section, 'shelf': shelf}
        return f'Book location set to Section: {section}, Shelf: {shelf}'
        
    @staticmethod
    def is_new(year):
        current_year = int(2024)
        return year > current_year - 5

class File:
    def __init__(self, file_type, file_size):
        self.ftype = file_type
        self.fsize = file_size
    
    def file_info(self):
        return f"File Type: {self.ftype}, File Size: {self.fsize} MB"

class EBook(Book, File):
    
    def __init__(self, title, author, published_year, file_type, file_size, location=None):
        Book.__init__(self, title, author, published_year, location)
        File.__init__(self, file_type, file_size)  
        
    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, {self.file_info()}"

class AudioBook(Book):
    
    def __init__(self, title, author, published_year, narrator_name, length):
        super().__init__(title, author, published_year)
        self.narrator = narrator_name
        self.length = length
        
    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Narrator: {self.narrator}, Length: {self.length} hours"

books = []
    
while True:
    print("\nChoose an option:")
    print("1. Add Book")
    print("2. Add E-Book")
    print("3. Add Audio Book")
    print("4. Show All Books")
    print("5. Set Location for a Book")
    print("6. Exit")
        
    choice = input("Enter your choice: ")
        
    if choice == '1':
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        published_year = int(input("Enter published year: "))
        books.append(Book(title, author, published_year))
    elif choice == '2':
        title = input("Enter e-book title: ")
        author = input("Enter author name: ")
        published_year = int(input("Enter published year: "))
        file_type = input("Enter file type (e.g., PDF): ")
        file_size = float(input("Enter file size (MB): "))
        books.append(EBook(title, author, published_year, file_type, file_size))
    elif choice == '3':
        title = input("Enter audio book title: ")
        author = input("Enter author name: ")
        published_year = int(input("Enter published year: "))
        narrator_name = input("Enter narrator name: ")
        length = float(input("Enter length (hours): "))
        books.append(AudioBook(title, author, published_year, narrator_name, length))
    elif choice == '4':
        print("\nAll Books:")
        for book in books:
            print(book.get_info())
    elif choice == '5':
        print("\nSelect a book to set its location:")
        for idx, book in enumerate(books):
            print(f"{idx + 1}. {book.title()}")
        book_index = int(input("Enter book number: ")) - 1
        
        if 0 <= book_index < len(books):
            if isinstance(books[book_index], Book) and not isinstance(books[book_index], (EBook, AudioBook)):
                shelf = input("Enter shelf: ")
                section = input("Enter section: ")
                print(books[book_index].set_location(shelf, section))
            else:
                print("Location can only be set for physical books.")
        else:
            print("Invalid book number.")
    elif choice == '6':
        break
    else:
        print("Invalid choice. Please try again.")
