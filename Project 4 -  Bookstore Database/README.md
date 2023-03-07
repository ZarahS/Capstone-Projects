# Project 4 - Bookstore Database
>A program that allows a bookstore clerk to manage books stored in a database. This program uses SQL to allow the user to add new books, update existing books, delete books and search books in the database.

## Contents 
1. [Program Features](https://github.com/ZarahS/Capstone-Projects/tree/main/Project%204%20-%20%20Bookstore%20Database#1-program-features)
2. [Usage](https://github.com/ZarahS/Capstone-Projects/tree/main/Project%204%20-%20%20Bookstore%20Database#2-usage)
    - [Main Menu](https://github.com/ZarahS/Capstone-Projects/tree/main/Project%204%20-%20%20Bookstore%20Database#main-menu)
    - [Add Book](https://github.com/ZarahS/Capstone-Projects/tree/main/Project%204%20-%20%20Bookstore%20Database#add-book)
    - [Update Book](https://github.com/ZarahS/Capstone-Projects/tree/main/Project%204%20-%20%20Bookstore%20Database#update-book)
    - [Delete Book](https://github.com/ZarahS/Capstone-Projects/tree/main/Project%204%20-%20%20Bookstore%20Database#delete-book)
    - [Search Book](https://github.com/ZarahS/Capstone-Projects/tree/main/Project%204%20-%20%20Bookstore%20Database#search-book)

## 1. Program Features

This program is made up of 4 key functions that a user can perform:

| Function  |Description|
|:---:|---|
|Add Book|Allows user to enter a new book into the database|
|Update Book|Allows user to update existing book|
|Delete Book|Allows user to delete a book from the database|
|Search Book|Allows user to search for a book|

The database has 4 fields which include:
- Unique ID
- Book Title
- Author
- Quantity


## 2. Usage

To run the program, enter the following into the terminal:
```
python bookstore.py
```

### Main Menu

The main menu provides the user with the following selections:

```
-----------------------------BOOKSTORE SYSTEM MENU------------------------------
                
Welcome to your book store management system!
                
Please select one of the following options: 
                 
1 - Add a book                
2 - Update book                
3 - Delete book                
4 - Search books                
0 - Exit                

--------------------------------------------------------------------------------
```

### Add Book

If the user selects option 1, they are prompted to create a new record in the database:

```
Enter book id: 
Enter book title:
Enter book author:
Enter book quantity:

```
If the record is successfully created, the user will see the following message:

```
Your book has been added successfully:

ID -  3001
Title -  A Tale of Two Cities
Author -  Charles Dickens
Quantity -  30
```

### Update Book

If the user selects option 2, they are asked to enter the ID of the book they would like to update:

```
Enter the ID of the book you would like to update: 3002
```
If the user has entered an ID that exists in the database, the record for that book is shown and the user is asked which field they would like to update:

```
Current record for book with ID 3002:

Title: Harry Potter and the Philosopher's Stone
Author: J.K. Rowling
Quantity: 40

Enter the number of the field you want to update: 
1. Title
2. Author
3. Quantity
```
Once the user has chosen a field to update, the database is updated and the new record is printed:
```
Enter new quantity: 40

Updated record for book with ID 3002:

Title: Harry Potter and the Philosopher's Stone
Author: J.K. Rowling
Quantity: 40
```

### Delete Book

If the user selects option 3, a table depicting all the existing records in the database is printed and the user is requested to enter the ID of the book they would like to delete from the system:

```
+------+------------------------------------------+-----------------+-------+
|   ID | Title                                    | Author          |   Qty |
+======+==========================================+=================+=======+
| 3001 | A Tale of Two Cities                     | Charles Dickens |    30 |
+------+------------------------------------------+-----------------+-------+
| 3002 | Harry Potter and the Philosopher's Stone | J.K. Rowling    |    50 |
+------+------------------------------------------+-----------------+-------+
| 3003 | The Lion, the Witch and the Wardrobe     | C. S. Lewis     |    25 |
+------+------------------------------------------+-----------------+-------+
| 3004 | The Lord of the Rings                    | J.R.R Tolkien   |    37 |
+------+------------------------------------------+-----------------+-------+
| 3005 | Alice in Wonderland                      | Lewis Carroll   |    12 |
+------+------------------------------------------+-----------------+-------+
Enter the ID of the book to delete:

```
When an ID has been entered, the program checks to make sure that the user would like to delete this book:
``` 
Are you sure you want to delete 'The Lion, the Witch and the Wardrobe' by C. S. Lewis? (Y/N): 
```
When the user enters 'Y', the book is deleted from the database:
```
Book with ID 3003 has been deleted.
```

### Search Book

If the user selects option 4, they are requested to enter either the ID, title or author of the book they would like to find:

```
Enter the book ID, title or author to search: 
```
If a match is found, the user is presented the information:
```
The following books matched your search:

ID: 3005
Title: Alice in Wonderland
Author: Lewis Carroll
Qty: 12
```


