
books = {}

def show_option():
    print("1. Add Book")
    print("2. Search Book")
    print("3. Display Inventory")
    print("4. Exit")
    print("Enter an option")
    choice = int(input())
    return choice


def add_book():
    book_title = input("Enter Book Title: ")
    author_name = input("Enter Author Name: ")
    books[len(books) + 1] = {"title": book_title, "author": author_name}
    print("Book added successfully!")


def search_book():
    book_id = int(input("Enter Book Id: ")) 
    book = books.get(book_id)
    if book:
        print(f"Title: {book['title']}, Author: {book['author']}")
    else:
        print("Book Not Found")


def display_inventory():
    if not books:
        print("No Book Found")
    for book_id, book in books.items():
        print(f"ID: {book_id}, Title: {book['title']}, Author: {book['author']}")


def exit():
    print("Thankyou! Visit Again")


def process_choices(choice):
    if choice == 1:
        add_book()
        process_choices(show_option()) 
    elif choice == 2:
        search_book()
        process_choices(show_option()) 
    elif choice == 3:
        display_inventory()
        process_choices(show_option()) 
    elif choice == 4:
        exit()
    else:
        print("Invalid Choice ! Try Again")
        process_choices(show_option()) 


process_choices(show_option())



    
