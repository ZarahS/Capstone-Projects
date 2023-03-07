# Project 4 - Bookstore Database
>A program that allows a bookstore clerk to manage books stored in a database. This program uses SQL to allow the user to add new books, update existing books, delete books and search books in the database.

## Contents 
1. [Program Features](https://github.com/ZarahS/Capstone-Projects/tree/main/Project%204%20-%20%20Bookstore%20Database#1-program-features)
2. [Usage](https://github.com/ZarahS/Capstone-Projects/tree/main/Project%204%20-%20%20Bookstore%20Database#2-usage)

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
Once the user has chosen a field to update, the database is also updated and the new record is printed:
```
Enter new quantity: 40

Updated record for book with ID 3002:

Title: Harry Potter and the Philosopher's Stone
Author: J.K. Rowling
Quantity: 40
```

### Delete Book

### Search Book
