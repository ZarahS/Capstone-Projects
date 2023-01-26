# program that allows user to acccess two different financial calculators:
# an investment calculator and a home loan repayment calculator

import math

# request user to chose which calculator they would like to run
chosen_program = input("Choose either 'investment' or 'bond' from the menu below to proceed:"
"\ninvestment  -  to calaculate the amount of interest you'll earn on your investment"
"\nbond        -  to calculate the amount you'll have to pay on a home loan "
"\n")

# standardise user entry by converting chosen_program to lowercase
lowercase_chosen_program = chosen_program.lower()

# if investment is selected, request user to input deposit amount, interest rate, years investing and to choose between simple or compound interest
# standardise interest by converting user input to lowercase
if lowercase_chosen_program == "investment":
    deposit = float(input("Please enter the amount of money you are depositing \n£"))
    interest_rate = float(input("Please enter your interest rate \n")) / 100
    years_investing = int(input("Please enter the number of years you are investing \n"))
    interest = input("Would you like to opt for simple or compound interest? \n")
    lowercase_interest = interest.lower()

    # if user selects simple, use simple equation to print total interest to two decimal places
    # else if compound is selected, run the same steps as above but with a different formula
    # else print error message
    if lowercase_interest == "simple":
        total_interest = deposit * (1 + (interest_rate * years_investing))
        print(f"Your total amount with simple interest is £{total_interest:.2f}" )
    elif lowercase_interest == "compound":
        total_interest = deposit * math.pow((1+interest_rate), years_investing)
        print(f"Your total amount with compound interest is £{total_interest:.2f}")
    else:
        print("There has been an error, please try again")

# else if bond is selected, request user to enter house value, interest rate and repayment months
# these values are plugged into the montly bond repayment formula
# print monthly repayment amount to two decimal place
elif lowercase_chosen_program == "bond":
    house_value = float(input("Please enter the present value of the house \n£"))
    interest_rate = float(input("Please enter your interest rate \n")) / 100
    repayment_months = float(input("Please enter the number of months to repay the bond \n"))
    monthly_interest_rate = interest_rate /12
    monthly_bond_repayment = (monthly_interest_rate * house_value) / (1 - (1+ monthly_interest_rate)**(-repayment_months))
    print(f"Your total monthly repayment is £{monthly_bond_repayment:.2f}")

# else print error statment requesting user to rerun the program
else:
    print("There has been an error, please check yoour inputs and rerun the program") 