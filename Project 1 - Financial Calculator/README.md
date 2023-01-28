# Project 1 - Financial Calculator
> A simple financial calculator that allows the user to calculate their interest on an investment or calculate their monthly repayment amount on a home loan.

## Contents
 1. [Types of Interest](https://github.com/ZarahS/Capstone-Projects/edit/main/Project%201%20-%20Financial%20Calculator/README.md#1-types-of-interest)
 2. [Equations](https://github.com/ZarahS/Capstone-Projects/edit/main/Project%201%20-%20Financial%20Calculator/README.md#2-equations)
 3. [Usage](https://github.com/ZarahS/Capstone-Projects/edit/main/Project%201%20-%20Financial%20Calculator/README.md#3-usage)

## 1. Types of Interest

Interest is a fee for borrowing money. It is usually a percentage of the amount borrowed or saved. When you borrow money, the lender will charge you interest. When you save money, the bank will pay you interest. There are 2 types of interest, simple and compound.

### *Simple Interest*

Simple interest is a type of interest where the interest is calculated only on the initial principal amount, without taking into account the accumulated interest from previous periods. This means that the interest does not earn interest and the interest amount remains the same for the life of the loan or savings account.

### *Compound Interest*

Compound interest is where the interest is calculated on the initial principal amount, but also on the accumulated interest from previous periods. This means that the interest earns interest, leading to a faster growth of the investment or debt. The interest is usually compounded on a regular basis, such as annually or monthly.

### *Bond Repayment*

A home bond repayment refers to the process of paying back the principal amount of a home bond loan, plus any accumulated interest, to the lender. A home bond is a type of loan that is used to purchase a house or property. The home bond repayment is usually paid monthly over a specified loan term. The exact amount of a monthly home bond repayment will depend on the size of the loan, the interest rate, and the loan term.


## 2. Equations

This calculator utilises 3 different equation types:

| Type        | Equation          | Description  |
|:-------------:|-------------|-----|
| Simple Interest| $$\ P(1 + r \times t) $$ |*P* = the amount the user deposits, *r* = interest perecentage divided by 100 and *t* = number of years the money is being invested.|
| Compound Interest| $$\ P(1 + r)^{t} $$    |As above|
|Bond Repayment |  $$\ \frac{i\times P}{1 - (1 + i) \^{-n}} $$  | *i* = the monthly interest rate, *P* = present value of the house and *n* = the number of months over which the bond will be paid. |


## 3. Usage

To run the program, enter the following into the terminal:
```python 
python finance_calculators.py
```

The following menu will load:

```
Choose either 'investment' or 'bond' from the menu below to proceed:
investment  -  to calculate the amount of interest you'll earn on your investment
bond        -  to calculate the amount you'll have to pay on a home loan
```

If the user selects 'investment' they are requested to input the following information 
```
Please enter the amount of money you are depositing 
Please enter your interest rate 
Please enter the number of years you are investing 
```
The user is then given the option to select the interest type
``` 
Would you like to opt for simple or compound interest? 
```
The output is the investment amount
```
Your total amount with simple interest is £ 
```
If the user selects 'bond' they are requested to input the following information:
```
Please enter the present value of the house
Please enter your interest rate
Please enter the number of months to repay the bond
```
The output is the monthly bond repayment

```
Your total monthly repayment is £ 
```

