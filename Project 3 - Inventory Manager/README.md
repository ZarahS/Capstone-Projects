# Project 3 - Inventory Manager
>A shoe inventory management program built to optimise delivery time and improve stock organisation. THis program utilises object-oriented programming (OOP) to allows users to search products by code, log a new product, determine the product with the lowest quantity and restock it, determine the product with highest quantity and calculate the total value of each stock item. 

## Contents 
1. [Program Features](https://github.com/ZarahS/Capstone-Projects/tree/main/Project%203%20-%20Inventory%20Manager#1-program-features)
2. [Usage](https://github.com/ZarahS/Capstone-Projects/tree/main/Project%203%20-%20Inventory%20Manager#2-usage)
   - Inventory Menu
   - Record Shoe
   - View Shoes
   - Restock Shoes
   - Search Shoes
   - View Shoe Values
   - View Shoe Sale
   - Exit points

## 1. Program Features

This program is made up of 6 key functions that a user can perform:

| Function  |Description|
|:---:|---|
|Record a shoe| Allows user to enter a new shoe into the inventory |
|View shoes| Allows user to view all shoes in inventory|
|Restock shoes|Allows user to view shoes with least stock and choose which shoe they would like to restock|
|Search shoes|Allows a user to obtain shoe information via shoe code|
|View shoe values|Allows user to view value of each shoe product in the inventory
|View shoe sale|Allows user to view the sale price for the product with the highest quantity|

Shoe products are stored in the inventory.txt file with the following information:
- Country
- Code
- Product
- Cost
- Quantity

## 2. Usage

To run the program, enter the following into the terminal:
```
python inventory.py
```
### Inventory Menu

The program initates by printing a menu selection:

```
-------------------------------INVENTORY MENU------------------------------
                
Welcome to the shoe inventory system!
                
Please select one of the following options: 
                 
1 - Record Shoe                
2 - View Shoes                
3 - Restock Shoes                
4 - Search Shoes                
5 - View Shoe Values                 
6 - View Shoe Sale                 
7 - Exit      
---------------------------------------------------------------------------
```
### 1 - Record Shoe
If the user select this option, the following information is requested:
```
Please enter the product country: 
Please enter the product code:
Please enter the product name:
Please enter the product cost as an integer:
Please enter the product quantity as an integer:
```
Once the appropriate values are entered, these values are written to the inventory.txt file and the following message is printed:
```
New item [UK, SKU12345, Air Max, 100, 3000] has been succesfully recorded.
```
### 2 - View Shoes
This selection will print out all the shoes stores from the inventory in a user-friendly table format

```
----------------------------INVENTORY LIST---------------------------
+---------------+----------+---------------------+-------+----------+
|    Country    |   Code   |       Product       | Cost  | Quantity |
+---------------+----------+---------------------+-------+----------+  
|      UK       | SKU12345 |       Air Max       |  100  |   3000   |
+---------------+----------+---------------------+-------+----------+

```
### 3 - Restock Shoes

This feature will print out a table, in the same format as above, with the 5 shoe items that are lowest in stock. The user will then be asked:
```
Would you like to update the stock levels for any of these shoes? (y/n)
```
If the user choses to update the stock, they will then be asked:

```
Please enter the index of the product you would like to update:
Please enter the new stock value:
```
The new stock value entered must be greater than the current stock level, if this condition is met, the inventory txt file is updated for that shoe product.

### 4 - Search Shoes

When this option is selected the user is requested:

```
Please enter the code you are searching for:
```
If the product code  matches a shoe stored in the inventory then the shoe information is printed to the terminal:

```
Shoe information

Product: Air Max
Country: UK
Code: SKU12345
Cost: 100
Quantity: 3000
```
### 5 - View shoe values

This option generates a table with two columns, one is for the product and one is for values, the values are obtained by muliplying the cost by quantity.

```
----------PRODUCT VALUES---------
+---------------------+--------+
|       Product       | Value  |
+---------------------+--------+
|       Air Max       | 300000 | 
+---------------------+--------+
```
### 6 - View shoe sale

When the user makes this selection the shoe with the highest quantity is printed to the terminal as for sale:

```
-------------FOR SALE-------------

Product: Air Max
Country: UK
Code: SKU12345   
Quantity: 3000
Old Price: £100
Sale Price: £75
----------------------------------
```
### Exit points

There are 2 exit points within this program, the first is found in the main menu and the second is found at the end of completing options 1-6:

```
Please select one of the following options:
            
m - Return to main menu             
e - Exit
```
