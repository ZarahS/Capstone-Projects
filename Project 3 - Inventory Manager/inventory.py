#===================================================OOP INVENTORY PROGRAM============================================================

from tabulate import tabulate

#==========================================================CLASS=====================================================================

class Shoe:

    # intialize shoe class with country, code, product, cost and quantity
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # functions created to access each parameter
    def get_product(self):
        return self.product
       
    def get_cost(self):
        return self.cost

    def get_code(self):
        return self.code

    def get_quantity(self):
        return self.quantity

    def get_country(self):
        return self.country

    # function that returns object as a str
    def __str__(self):
        return f"{self.country},{self.code},{self.product},{self.cost},{self.quantity}"

#=========================================================FUNCTIONS==================================================================

# empty list to store shoe objects
shoe_list = []

# reads shoe data
def read_shoes_data():

    # try to open file for reading
    try:
            # open inventory file for reading
            with open("inventory.txt", "r") as inventory_file:

                # skips header line
                next(inventory_file)
                # iterates through each line in inventory file:
                for line in inventory_file:

                    # strip \n from end of each line and split using the comma as the delimeter
                    line = line.strip("\n").split(",")

                    # shoe object created which calls on Shoe class and takes in split string as parameters
                    shoe_object = Shoe(line[0], line[1], line[2], line[3], line[-1])

                    # append shoe object to shoe list
                    shoe_list.append(shoe_object)

    # except statement handles file not found error
    except FileNotFoundError as error:
            print("\n" + str(error) + "\n")
            return False

# records new shoes
def capture_shoes():
    
    # while loop which checks user input
    while True: 

        # request user for inputs
        new_country = input("Please enter the product country:\n")
        new_code = input("Please enter the product code:\n")
        new_product = input("Please enter the product name:\n")
        new_cost = input("Please enter the product cost as an integer:\n")
        new_quantity = input("Please enter the product quantity as an integer:\n")

        user_input = str(new_country + new_code + new_product + new_quantity)

        try:

            # checks if values entere are integers
            int(new_cost)
            int(new_quantity)
        
            # if user has not entered a suffienct number of characters print error message
            if len(user_input) <= 15:
                print("\nError, you have not entered sufficient characters, please try again!\n")

            # else create new shoe object and to txt file
            else:
                
                # create a new shoe object to store values
                new_shoe = Shoe(new_country, new_code, new_product, new_cost, new_quantity)

                # # append new shoe object to shoe list
                shoe_list.append(new_shoe)

                # open inventory.txt in append mode and write new data to file and print success message
                with open ("inventory.txt", "a") as inventory_update:    
        
                    inventory_update.write(f"\n{new_country},{new_code},{new_product},{new_cost},{new_quantity}")
                    print(f"\nNew item: [{shoe_list[-1].__str__()}] has been succesfully recorded.")

                # break out of while loop
                break
        
        # except if value error, print error messsage
        except:
            if ValueError:
                print("\nError, you have not entered an integer, please try again.\n")

# allows user to view inventory
def view_all():

    # prints title
    print("\n" + "INVENTORY LIST".center(75, "-") + "\n")

    # sets header columns 
    columns = ["Country", "Code", "Product", "Cost", "Quantity"]

    # data stored in table list
    table = []
    country = []
    code = []
    product = []
    cost = []
    quantity = []

    # iterates through each shoe object in list to fetch object items and append to respective lists
    for shoe_object in shoe_list:
        country.append(shoe_object.get_country())
        code.append(shoe_object.get_code())
        product.append(shoe_object.get_product())
        cost.append(shoe_object.get_cost())
        quantity.append(shoe_object.get_quantity())
    
    # values passed into zip function and stored in table
    table = zip(country, code, product, cost, quantity)
    
    # table format set to pretty and table is printed using tabulate 
    print(tabulate(table, headers=columns, tablefmt="pretty"))

    print("\n" + "END".center(75, "-") + "\n")

# allows user to restock low quanitiy items
def re_stock():

    # flag to check if stock has been updated succesfully
    stock_flag = False

    # empty lists to store values
    restock_shoes = []
    table = []
    country = []
    code = []
    product = []
    cost = []
    quantity = []

    # columns for table
    columns = ["Country", "Code", "Product", "Cost", "Quantity"]
    
    # sort shoe list by quantity
    shoe_list.sort(key=lambda x: int(x.quantity))

    # iterate through shoe list and append 5 shoes to restock_shoes list
    for shoe in range(0,5):
        restock_shoes.append(shoe_list[shoe])
    
    # iterate through restock shoes and access country, code, product, cost and quanity for shoes with least stock
    for line in restock_shoes:
        country.append(line.get_country())
        code.append(line.get_code())
        product.append(line.get_product())
        cost.append(line.get_cost())
        quantity.append(line.get_quantity())

    # values passed into zip function and stored in table
    table = zip(country, code, product, cost, quantity)

    # print header and table
    print("\n" + "LOWEST STOCK".center(75, "-") + "\n")
    print(tabulate(table, headers=columns, tablefmt="pretty")+ "\n")
    
    # ask user if they would like to update stock 
    stock_update = input("Would you like to update the stock levels for any of these shoe? (y/n)\n").lower()
    
    # while loop to verify user entries
    while True:

            # if user selects y:
            if stock_update == "y":

                try:
                    
                    # request user to enter index of product and new values, these are stored as type int
                    stock_index = int(input("\nPlease enter the index of the product you would like to update:\n"))
                    updated_stock = int(input("\nPlease enter the new stock value: \n"))
                    
                    # array stores information of selected stock index
                    stock_array = ((restock_shoes[stock_index]).__str__()).split(",")
                    
                    # product name extracted from array and stored in product variable
                    product = stock_array[2]

                    # new stock quanity is updated in stock array
                    stock_array[-1] = updated_stock

                    # new file created containing header
                    updated_file = ""
                    
                    # open inventory file for reading
                    inventory_file = open("inventory.txt", "r")

                    # iterate through inventory.txt, convert string to list format
                    for line in inventory_file.readlines():
                        line = line.split(",")

                        # if a line has the product that needs updating:
                        if line[2] == product:
                            
                            # if updated stock is lower than or equal to current numb, print error message and add existing line
                            if int(line[-1]) >= int((updated_stock)):
                                print("\nError, new stock value cannot be lower than or equal to current stock level!")
                                line = (",").join(line)
                                updated_file += line
                                
                            # else replace line with new line and add this to updated_file, print success message and break loop
                            else:
                                new_line = (",").join(map(str, stock_array))
                                updated_file += new_line + "\n"
                                stock_flag = True
                        
                        # else if there is no match keep old line and add to updated file
                        else:
                            line = (",").join(line)
                            updated_file += line
                        
                    inventory_file.close()

                    # open inventory.txt for writing and write updated file to it
                    output_file = open("inventory.txt", "w")
                    output_file.writelines(updated_file)
                    output_file.close()

                    # if stock flag is true, print success message and break out of loop
                    if stock_flag == True:
                        print(f"\nFile has been updated succesfully: {stock_array} \n", )
                        break
                
                # exception picks up valueError and prints error message
                except ValueError:
                    print("\nError invalid input, please try again.")
                
                # exception picks up any index errors and prints relevant message
                except IndexError:
                    print("\nError, index number is out of range, enter a value in range 0-4.\n")
                
            # else if user selects n break from loop
            elif stock_update == "n":
                break

            # else print error
            else:
                print("\nError, stock could not be updated.\n")
                break

# allows user to search shoe by SKU code
def search_shoe():

    # empty string to store found product and flag to check if product has been found
    found_product = ""
    found_product_flag = False

    print("\n" + "SEARCH PRODUCT".center(75, "-") + "\n")

    while True:
            # request user to enter a code
            code = input("\nPlease enter the code you are searching for:\n")

            # iterate through shoe_list
            for shoe_object in shoe_list:
                
                # if a shoe code matches user code, add line to found_product and call on str function to print
                if shoe_object.get_code() == code:

                    found_product += shoe_object.__str__()
                    print(f"\nShoe information: {found_product}\n\n" + "-"* 75)

                    # flag marked as True and break inner while loop
                    found_product_flag = True
                    return

            # if flag remains false, print error message and ask user to try again
            if found_product_flag == False:
                print("Error, you have not entered a valid shoe code, please try again!")
                continue

# displays value of inventory items
def value_per_item():

    # header columns set
    columns = ["Product", "Value"]

    # empty array to store values
    values_table = []

    # iterate through shoe list and muliply cost and quantity values and append info to values table
    for shoe_object in shoe_list:
        val = int(shoe_object.get_cost()) * int(shoe_object.get_quantity())
        product = shoe_object.get_product()
        product_val = [product, val]
        values_table.append(product_val)

    # prints table with header
    print("\n" + "PRODUCT VALUES".center(33, "-"))
    print("\n" + (tabulate(values_table, headers=columns, tablefmt="pretty")) + "\n")

# marks highest quantity item as for sale
def highest_qty():
        
    # print header
    print("\n" + "FOR SALE".center(75, "-") + "\n")

    # retrieves max quantity item from shoe_list
    highest_quantity = max(shoe_list, key=lambda item: int(item.quantity))

    # extract each data item from the max object
    country = highest_quantity.get_country()
    code = highest_quantity.get_code()
    product = highest_quantity.get_product()
    cost = highest_quantity.get_cost()
    quantity = highest_quantity.get_quantity()

    # print item as for sale with new price 
    print(f"Product: {product}\nCountry: {country}\nCode: {code}\
        \nQuantity: {quantity}\nOld Price: £{cost} \nSale Price: £" + str(int(cost)-300) + "\n" + "-"*75)

# allows user to return to main menu or exit program
def exit_selection():
    
    while True:

        # allow user to exit program or continue to main menu
        exit_program = input("\nPlease select one of the following options:\n\
            \nm - Return to main menu \
            \ne - Exit\n\n" )

        # if user selects m, return to main menu
        if exit_program == "m":
            return

        # else if e is selected exit program
        elif exit_program == "e":
            exit()
        
        # else print error message
        else:
            print("Error, incorrect selection")

#========================================================MAIN FUNCTION================================================================

# main function
def __main__():

    # call on read shoes data
    read_shoes_data()

    # while loop which checks user entries
    while True:

        try:

            # requests user to select a menu option
            menu = (input("\n" + "INVENTORY MENU".center(75, "-") + "\n\
                \nWelcome to the shoe inventory system!\n\
                \nPlease select one of the following options: \n \
                \n1 - Record Shoe\
                \n2 - View Shoes\
                \n3 - Restock Shoes\
                \n4 - Search Shoes\
                \n5 - View Shoe Values \
                \n6 - View Shoe Sale \
                \n7 - Exit \
                \n\n" + "-"*75 + "\n\n"))

            # if 1 is selected, call on capture_shoes and exit_selection function
            if menu == "1":
                capture_shoes()
                exit_selection()
            
            # elif 2 is selected, call on view_all and exit_selection function
            elif menu == "2":
                view_all()
                exit_selection()
            
            # elif 3 is selected, call on re_stock and exit_selection function
            elif menu == "3":
                re_stock()
                exit_selection()

            # elif 4 is selected, call on view_all and exit_selection function
            elif menu == "4":
                search_shoe()
                exit_selection()
            
            # elif 5 is selected, call on values_per_item and exit_selection function
            elif menu == "5":
                value_per_item()
                exit_selection()

            # elif 6 is selected, call on highest_qty and exit_selection function
            elif menu == "6":
                highest_qty()
                exit_selection()
            
            # else print invalid value
            elif menu == "7":
                print("\nGoodbye!\n")
                exit()
        
            elif int(menu) > 7:
                print("\nYou have selected an incorrect number, please try again.")

        # print exception error
        except ValueError:
            print("Incorrect selection, you have not entered a number, please try again.")

# call on main function
__main__()