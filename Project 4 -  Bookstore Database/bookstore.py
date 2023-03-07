#=============================================BOOKSTORE DATABASE PROGRAM====================================================

# import modules
import sqlite3
from tabulate import tabulate

# create database connection
conn = sqlite3.connect('ebookstore.db')

cursor = conn.cursor()

# deletes existing table so that there is not an error when python file is run
conn.execute('''DROP TABLE books''')

# create table
conn.execute('''CREATE TABLE IF NOT EXISTS books
             (id INT PRIMARY KEY NOT NULL,
             title TEXT NOT NULL,
             author TEXT NOT NULL,
             qty INT NOT NULL);''')

# intial records are stored in 'books'
books = [(3001, 'A Tale of Two Cities', 'Charles Dickens', 30),
         (3002, "Harry Potter and the Philosopher's Stone", 'J.K. Rowling', 40),
         (3003, 'The Lion, the Witch and the Wardrobe', 'C. S. Lewis', 25),
         (3004, 'The Lord of the Rings', 'J.R.R Tolkien', 37),
         (3005, 'Alice in Wonderland', 'Lewis Carroll', 12)]

# iterate through books and insert each row into the table
for book in books:
    conn.execute("INSERT INTO books (id, title, author, qty) VALUES (?, ?, ?, ?)", book)

# function to add new book to the database
def add_book():

    while True:

        try:
            print("\n" + "ADD BOOK".center(50, "-"))

            # request user to enter book id for the new book
            id = int(input("\nEnter book id: "))

            # check if ID already exists in database and produce error statment if it does
            result = conn.execute("SELECT * FROM books WHERE id = ?", (id,))
            if result.fetchone():
                print("\nError: This ID already exists in the database, please enter a unique ID.\n")
                continue
            
            # ask user to enter title, author and quantity
            title = input("\nEnter book title: ")
            author = input("\nEnter book author: ")
            qty = int(input("\nEnter book quantity: "))

            # check if user has not entered values for title or author
            if not title or not author:
                raise NameError

            # insert new book into the table
            conn.execute("INSERT INTO books (id, title, author, qty) VALUES (?, ?, ?, ?)", (id, title, author, qty))
            conn.commit()

            # print success message and return to main menu
            print("\nYour book has been added successfully:\n\nID - ", str(id) + "\nTitle - ", title + "\nAuthor - ", author +
            "\nQuantity - ", str(qty))
            return

        except ValueError:
            print("\nError - You have not entered a valid input, please try again")
            continue

        except NameError:
            print("\nTitle and author fields cannot be empty, please try again.")

# function to update book information
def update_book():

    while True:

        try:
            print("\n" + "UPDATE BOOK".center(50, "-"))

            # Request user to input ID of book to update
            id = int(input("\nEnter the ID of the book you would like to update:\n"))
            
            # Check if book ID exists in database, if not raise a ValueError
            cursor = conn.execute("SELECT * FROM books WHERE id = ?", (id,))
            row = cursor.fetchone()
            if row is None:
                raise ValueError("\nBook with ID %d does not exist, please try again.\n" % id)

            # print current record for relevant ID
            print("Current record for book with ID %d:\n" % id + "\nTitle:", row[1] + "\nAuthor:", row[2] + "\nQuantity:", row[3])
            
            # Ask user which field to update, raise error if invalid number is entered
            choice =int(input("\nEnter the number of the field you want to update: \n1. Title\n2. Author\n3. Quantity\n"))
            if choice not in [1, 2, 3]:
                raise ValueError("Invalid field number.\n")
            
            # prompt user for new value depending on which field they are updating 
            if choice == 1:
                new_value = input("\nEnter new title: ")
                conn.execute("UPDATE books SET title = ? WHERE id = ?", (new_value, id))

            elif choice == 2:
                new_value = input("\nEnter new author: ")
                conn.execute("UPDATE books SET author = ? WHERE id = ?", (new_value, id))

            else:
                new_value = input("\nEnter new quantity: ")
        
                # validate data type for quantity, if a number is not entered, raise error
                if not new_value.isdigit():
                    raise ValueError("Quantity must be an integer, please try again.\n")
                conn.execute("UPDATE books SET qty = ? WHERE id = ?", (int(new_value), id))
            
            # save changes to database
            conn.commit()
            
            # print success message and return to main menu
            cursor = conn.execute("SELECT * FROM books WHERE id = ?", (id,))
            row = cursor.fetchone()
            print("\nUpdated record for book with ID %d:\n" % id + "\nTitle:", row[1] + "\nAuthor:", row[2] + "\nQuantity:", row[3])
            return

        # exception to catch ValueErrors
        except ValueError as e:
            print("\nError:", e)

# function to delete book from database
def delete_book():

    while True:

        try:
            print("\n" + "DELETE BOOK".center(80, "-"))

            # fetch all rows in table and print using tabulate 
            c = conn.cursor()
            c.execute("SELECT * FROM books")
            rows = c.fetchall()
            print(tabulate(rows, headers=['ID', 'Title', 'Author', 'Qty'], tablefmt='grid'))

            # request user to enter id they would like to delete and verify it exists
            book_id = input("\nEnter the ID of the book to delete:\n")
            c.execute("SELECT * FROM books WHERE id=?", (book_id,))
            row = c.fetchone()

            # if id not in database, print error message
            if row is None:
                print(f"\nNo book found with ID {book_id}, please try again!\n")
            
            # else confirm if user would like to delete book
            else:
                confirm = input(f"Are you sure you want to delete '{row[1]}' by {row[2]}? (Y/N): ")

                # if user enters y, record is deleted
                if confirm.lower() == "y":
                    try:
                        c.execute("DELETE FROM books WHERE id=?", (book_id,))
                        conn.commit()
                        print(f"\nBook with ID {book_id} has been deleted.")
                        return

                    except:
                        print("\nError: Unable to delete book.")

                # else if user enters n, the record is not deleted and they return to the main menu
                elif confirm.lower() == "n": 
                    return
                
                # else a ValueError is raised
                else:
                    raise ValueError("Invalid entry, please try again!")

        # exception statement to catch any ValueErrors
        except ValueError as e:
            print("\nError:", e)

# function to search for a specific book
def search_book():

    print("\n" + "SEARCH BOOK".center(80, "-"))

    # request user to enter the ID, title or author they would like to search 
    search_term = input("\nEnter the book ID, title or author to search: ")
    found_book = []

    # retrieve books from the database
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()

    # iterate through records and check if user input matches any ids, titles or authors, if match, append to found_books list
    for book in books:
        if search_term.lower() == book[1].lower() or search_term.lower() == book[2].lower() or search_term == str(book[0]):
            found_book.append(book)

    # if book has been found print book info
    if found_book:
        print("\nThe following books matched your search:\n")
        for book in found_book:
            print(f"ID: {book[0]}\nTitle: {book[1]}\nAuthor: {book[2]}\nQty: {book[3]}\n")

    #  else print no match found
    else:
        print("No books matched your search.")

# main program loop
def __main__():

    while True:
        
        # menu that allows user to select which operation to run
        menu = (input("\n" + "BOOKSTORE SYSTEM MENU".center(80, "-") + "\n\
                \nWelcome to your book store management system!\n\
                \nPlease select one of the following options: \n \
                \n1 - Add a book\
                \n2 - Update book\
                \n3 - Delete book\
                \n4 - Search books\
                \n0 - Exit\
                \n\n" + "-"*80 + "\n\n"))

        try:
            choice = int(menu)
        
        except ValueError:
            print("\nIncorrect selection, you have not entered a number, please try again!")
            continue

        # if user selects 1, add_book function runs 
        if choice == 1:
            add_book()
        
        # elif user selects 2, update_book function runs 
        elif choice == 2:
            update_book()

        # elif user selects 3, delete_book function runs 
        elif choice == 3:
            delete_book()
        
        # elif user selects 4, search_book function runs 
        elif choice == 4:
            search_book()
        
        # elif user selects 0, exit program
        elif choice == 0:
            print("\nYou have successfully exited the program, see you next time!")
            return
       
        # else print error
        else:
            print("\nInvalid choice. Please try again.")

# call on __main__ function
__main__()

# close database connection
conn.close()
