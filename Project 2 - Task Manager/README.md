# Project 2 - Task Manager
> A task manager program that allows a small business to manage tasks assigned to team members. Users have the ability to create, edit and view tasks. The admin user is able to do all these functions as well as retrieve tasks statistics and generate reports.

## Contents
 1. [Program Features](https://github.com/ZarahS/Capstone-Projects/edit/main/Project%202%20-%20Task%20Manager/README.md#program-1-features)
 2. [Login](https://github.com/ZarahS/Capstone-Projects/edit/main/Project%202%20-%20Task%20Manager/README.md#2-login)
 3. [Usage](https://github.com/ZarahS/Capstone-Projects/edit/main/Project%202%20-%20Task%20Manager/README.md#2-usage) 
    - [Core Functions](https://github.com/ZarahS/Capstone-Projects/edit/main/Project%202%20-%20Task%20Manager/README.md#core-functions)
    - [Admin Functions](https://github.com/ZarahS/Capstone-Projects/edit/main/Project%202%20-%20Task%20Manager/README.md#admin-functions)
 

## 1. Program Features

This program is made up of 7 key functions with varying levels of access.

| Function  | Access  | Description  |
|:------:|:---:|--------------------------------|
| r - Register user  | Admin only |  Allows the admin user to generate a new user by entering a username and password. |
| a - Add task  | All users   | Allows users to create a new task, the user will be requested to input task title, description, due date and the user this task is assigned to.|
| va - View all tasks  | All users  | Allows the user to view all tasks in a user-friendly format.|
| vm - View my tasks | All users  | Allows the user to view tasks that are assigned to them and mark any of them as complete or edit the due date or the the user the task is assigned to. |
| gr - Generate reports  | Admin only |  Outputs 2 reports for the admin, one is a user overview report that provides a breakdown of number of tasks completed by users. The second is a task overview report, this analyses the percentage of incomplete and overdue tasks. |
| ds - Display statistics  | Admin only | Allows the admin to view the information from the reports in a user-friendly format.|
| e - Exit | All users | Allows user to log out of their account.|

## 2. Login

This program runs in two modes, an admin and a user mode.

To enter the program as an admin please use the following log on details:
``` 
Username: admin
Password: adm1n
```

To enter the progam as a user, please use the following log on details:
``` 
Username: john
Password: sm1th
```
## 3. Usage

To run the program, copy and paste the following code into the terminal:
```python 
python task_manager.py
```
The program is initiated with the user being requested to log on.
``` 
Please enter your username:
Pleae enter your password:
```
These inputs are validated and if they are accepted the user sees a welcome message.
``` 
Welcome, you have successfully logged into your account
``` 
If you enter the program as an admin user the following menu is loaded:
``` 
--------------------MENU--------------------
Please select one of the following options:
        r - Register a new user 
        a - Adding a task 
        va - View all tasks 
        vm - View my task 
        gr - Generate reports 
        ds - Display statistics
        ne - Exit 
--------------------------------------------
```

If you enter as a user, the following menu is loaded:

``` 
--------------------MENU--------------------
Please select one of the following options:
        a - Adding a task 
        va - View all tasks 
        vm - View my task 
        ne - Exit 
--------------------------------------------
```
### Core functions

There are 4 functions that all users can perform:

#### a - Adding a task

If the user selects this option, they are requested to input the following information:
``` 
Enter the username of the person you want to assign this task to:
Please enter the task title:
Please enter a task description: 
Please enter the task due date in format (DD Mon YYYY) : 
``` 
This information is written to the tasks.txt file.

#### va - View all tasks

This prints out a list of all the tasks stored in the tasks.txt file in a user-friendly format. Tasks are printed to the terminal in the following format:
``` 
Task Number: 1
Task: Example Task
Assigned to: John
Date Assigned: 10 Jan 2023
Due Date: 30 Jan 2023
Task Complete?: No
Task Description: Complete example task
``` 
#### vm - View my tasks

This function checks which user is logged on and extracts the tasks assigned to this user only and prints them out in the same format as above. The user is then asked which task number they would like to review and they are presented with this selection menu:
```
Please select one of the following options:              
ed - Edit the task                 
c - Mark as complete                 
-1 - Return to the main menu
 ```
If the user would like to make an edit, they are presented with a choice of what they would like to edit:
```
Please select what you would like to edit:                
u - user assigned to task                     
td - task due date
```
After a selection is made, the tasks.txt file is updated accordingly. Similarly, when the user chooses to mark the task as complete, the file is updated.

#### e - Exit

When the user selects this option the terminal prints out the following message:
``` 
You have logged out of your account, Goodbye!
```
 
### Admin functions

There are 3 functions that only the admin user will have access to, they are:

#### r - Register user
When the admin wants to register a user, the following information is requested:
``` 
Please enter the new username:
Please enter the new password:
Please confirm your new password:
```
The new username cannot be the same as an existing username and the passwords must match for this user to be created. These details are then stored in the user.txt file and allowing the user to log onto the system.

#### gr - Generate reports
When the admin selects this options two files will be created, a user_overview and task_overview txt file. 
The user_overview file will provide user stats:
```
---------------------------------------------------------------USER OVERVIEW REPORT---------------------------------------------------------------
Total users: 2
Total tasks generated: 5

User    Number of tasks assigned    % of tasks assigned    % of completed tasks    % of incomplete tasks    % of incomplete and overdue tasks
--------------------------------------------------------------------------------------------------------------------------------------------------
admin             1                        20                      100                      0                               0
John              4                        80                       50                     50                              20
```
The task_overview file will provide task stats in the format:

```
--------TASK OVERVIEW REPORT--------
Total tasks:                      5
Completed tasks:                  3
Incomplete tasks:                 2
Overdue & incomplete tasks:       1
Incomplete percentage:          40%
Overdue percentage              20%  
```
#### ds - Display statistics
This function will print out the user_overview and task_overview reports to the terminal for ease of viewing. The format will be the same as shown above.

