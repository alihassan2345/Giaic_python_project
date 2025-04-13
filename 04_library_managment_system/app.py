library = []

def view_library():
    if not library:
        print("Library is empty.")
    else:
        for idx, book in enumerate(library, start=1):
            print(f"{idx}. Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}, Year: {book['year']}")

def add_book():
    title = input("Enter the book title: ")
    author = input("Enter the author's name: ")
    genre = input("Enter the genre: ")
    year = input("Enter the publication year: ")
    library.append({'title': title, 'author': author, 'genre': genre, 'year': year})
    print("Book added successfully!")

def remove_book():
    title = input("Enter the title of the book to remove: ")
    for book in library:
        if book['title'].lower() == title.lower():
            library.remove(book)
            print(f"Book '{title}' removed successfully.")
            return
    print(f"Book '{title}' not found in the library.")

# Example usage
while True:
    print("\nLibrary Management System")
    print("1. View Library")
    print("2. Add Book")
    print("3. Remove Book")
    print("4. Exit")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        view_library()
    elif choice == '2':
        add_book()
    elif choice == '3':
        remove_book()
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice! Please try again.")
