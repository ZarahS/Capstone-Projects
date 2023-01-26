# Program to allow a small business to manage tasks assigned to team members

# import date class from datetime package
from datetime import date, datetime

# use date.today to obtain current day and store in today
today = date.today()

# function which fetches usernames and passwords from user.txt file
def user_login():

    # create an empty dictionary to store username and passwords
    users_dict = {}

    # open user text file
    with open("user.txt", "r", encoding="utf-8") as user_file:

        #  for each line in user.txt
        for line in user_file:

            # split string at the comma into 2 variables, user and password
            user, password = line.split(", ")

            # strip newline character from pasword
            password = password.strip("\n")

            # user is key and password is value for users_dict
            users_dict[user] = password

    # return dictionary of users and passwords
    return users_dict

# function which prints out tasks and tidies data 
def print_tasks(task_array):
   
    # index of task_array used to extract relevant data, concatenate and print tasks
    print("Task:             " + task_array[1])
    print("Assigned To:       " + task_array[0])
    print("Date Assigned:    " + task_array[-3])
    print("Due Date:         " + task_array[-2])
    print("Task Complete?    " + task_array[-1].replace("\n",""))
    print("Task Description:  "  + task_array[2].strip())

# function which prints out separate menu for admin and other users
def print_menu():

    # if user name is admin, display admin menu:
    if user_name == "admin":
        
        # menu is formatted with spacing and hyphens and user input is converted to lower case
        menu = (input("\n" + "MENU".center(63, "-") + "\n\
        \nPlease select one of the following options: \n \
        \nr - Register a new user \
        \na - Adding a task \
        \nva - View all tasks \
        \nvm - View my task \
        \ngr - Generate reports \
        \nds - Display statistics = Total number of tasks & users \
        \ne - Exit \
        \n--------------------------------------------------------------- \
        \n\n""")).lower()   
    
    # else display standard menu
    else:

        # menu is formatted with spacing and hyphens and user input is converted to lower case
        menu = input('''\n---------------------------------------------------------------\
        \nPlease select one of the following options below:\n \
        \na - Adding a task \
        \nva - View all tasks \
        \nvm - View my task \
        \ne - Exit \
        \n---------------------------------------------------------------\
        \n\n ''').lower()
    
    # return menu
    return menu

# function which registers new users 
def reg_user():

    # open user.txt in append mode:
    with open("user.txt", "a", encoding="utf-8") as user_file:
        
        # while loop runs until new user is successfully added
        while True:

            # request user to input new user, password and confirm password
            new_user = input("\nPlease enter the new username: \n").lower()

            # if new user is in user dictionary print error message and restarts while loop using continue
            if new_user in users:

                print("\nThis username has already been registered please create a different username\n")
                continue

            new_password = input("\nPlease enter the new pasword \n")
            confirm_pw = input("\nPlease confirm your password: \n")

            # if new password equals confirm password:
            if new_password == confirm_pw:
                
                # write new user to user.txt file and print success message
                user_file.write("\n" + str(new_user) + ", " + new_password)
                print("\nSuccess! New username has been registered.")
                break

            # else print failure message
            else:
                print("\nYour passwords do not match, please try again\n") 

# function which adds new tasks
def add_task():

    # open tasks.txt in append mode
    with open("tasks.txt", "a", encoding="utf-8") as task_file:
        
        # request user to input username to reassign task to
        task_username = input("\nEnter the username of the person you want to assign this task to: ")

        # if task_username not in users print error message and return to main menu
        if task_username not in users:
    
            print("\nThis user does not exist, please register a new user or select an existing user.")
            return

        # request user to enter task info
        task_title = input("\nPlease enter the task title: ")
        task_description = input("\nPlease enter a task description: ")
        task_date = input("\nPlease enter the task due date in format DD Mon YYYY : ")
             
        # current date stores today's daye in format (Day, abbreviated Month, Year)
        current_date = today.strftime('%d %b %Y')
            
        task_completed = "no\n"
             
        # concatenate user task values and write to tasks.txt with a line break 
        task_file.write(f"{task_username}, {task_title}, {task_description}, {current_date}, {task_date}, {task_completed}")

        # print success message
        print("\nYour task has been successfully added")

# function to view all oustanding tasks
def view_all(task_number):
    # open task file for reading
    with open("tasks.txt", "r", encoding="utf-8") as task_file: 
                
        # readlines in task_file and store in task
        task = task_file.readlines()
                
       # print header with centered formatting
        print("\n" + "ALL TASKS".center(130, "="))
                
        # for each line in task file:
        for line in task:
            
            # increment task number by 1
            task_number = task_number + 1

            # print task number
            print("\n\nTask Number:       " + str(task_number))

            # split line where there is a comma to create an array
            task_array = line.split(",")

            # use print_task functon to index, fetch required data and tidy as needed
            print_tasks(task_array)

        # print footer with centered formatting
        print("\n" + "END OF TASKS".center(130, "=") + "\n")

# function to allow user to view tasks assigned to them
def view_mine(task_number):

     # open tasks.txt in read mode and store in task_file:
    with open("tasks.txt", "r+", encoding="utf-8") as task_file:

        tasks = task_file.readlines()

        # empty variable replaced_file will store edits that are to be written to tasks.txt file
        replaced_file = ""

        # line counter set to 0
        i = 0
        
        # username is stored in a dictionary to track if user has tasks, set to false initially  
        no_task_flag = {user_name:False} 

        # print header for my tasks
        print("\n" + "MY TASKS".center(130, "="))

        # iterate through tasks.txt and increment task number with each loop
        for task in tasks:

            # task number incremented by 1 with each iteration
            task_number = task_number + 1

            # convert task from string to an array using comma as a delimiter 
            task_array = task.split(",")

            # if user_name declared at login by user is equal to a user in tasks file:
            if user_name == task_array[0]:
                
                # print task number of tasks assigned to user
                print("\nTask Number:       " + str(task_number))

                # call on print_task function for user task's
                print_tasks(task_array)
                
                # no task flag changes to True so no tasks assigned message will not be printed for user
                no_task_flag[user_name] = True
        
        # print footer for my tasks
        print("\n" + "END OF TASKS".center(130, "=") + "\n")

        # if no task flag for username is False, print no tasks message
        if no_task_flag[user_name] == False:
            print("\nYou have not been assigned any tasks.")

        # request user to enter number of task they would like to edit and cast as integer
        task_number = (input("\nPlease select the task number of the task you would like to review:\n"))
        
       # if task_number is a number & the task_number (casted) is less than or equal to length of tasks & not equal to 0:
        if task_number.isdigit() and int(task_number) <= len(tasks) and int(task_number) != 0 :
        
            # index task number is task number subtracted by 1
            index_task_num = int(task_number) -1

            # task array is index of tasks, this stores the specific task user wants to review
            task_array = tasks[index_task_num].split(",")

            # relevent task number and task is printed by calling on print_tasks function for array
            print("\nTask Number:       " + str(task_number))
            print_tasks(task_array)
            
            # task_completed stores the last item in the array which is yes/no
            task_completed = task_array[-1].strip("\n").strip(" ")

            # if task_completed is no:
            if task_completed == "no":

                # edit task menu is displayed, requesting user to input what they'd like to do
                edit_task= input("\n \
                \nPlease select one of the following options:\n \
                \ned - Edit the task \
                \nc - Mark as complete \
                \n-1 - Return to the main menu\n\n")

                # if user chooses to edit the task:
                if edit_task == "ed":
                    
                    # edit selection displayed, requesting further user input
                    edit_selection = input("\nPlease select what you would like to edit:\n \
                    \nu - user assigned to task \
                    \ntd = task due date\n\n").lower()
                    
                    # if user selects u:
                    if edit_selection == "u":

                        user_file = open("user.txt", "r")
                        user = user_file.readlines()

                        # store the user that the task is reassigned to in task_username 
                        task_username = input("\nEnter the username of the person you would like to reassign this task to:\n").lower()

                        # if task_username not in user ERORRR HERE 
                        if task_username not in users:

                            # print user does not exist message
                            print("\nTask cannot be reassigned as this user does not exist, please try again")

                        # else allow user to reassign task
                        else:

                            # task array at index 0 is made to equal the new task username
                            task_array[0] = task_username               

                            # task array is joined together as a string with new username
                            task_string = ",".join(task_array)
                            
                            # for task in tasks:
                            for task in tasks:

                                # if i (which is set to 0) is equivalent to index position of task number being reviewed
                                if i == index_task_num:
                                    
                                    # new line stores the replaced task string
                                    new_line = task.replace(task,task_string)
                                
                                # else new line is not changed and remains the same
                                else:
                                    new_line = task
                            
                                # each new_line is added to replaced_file
                                replaced_file = replaced_file + new_line

                                # i increments by 1 to iterate through tasks
                                i = i + 1
                            
                            # write replaced file to tasks.txt
                            write_file = open("tasks.txt", "w") 
                            write_file.write(replaced_file)
                            write_file.close()
                        
                            # print success message
                            print("\nYour task has been successfully edited")

                    # else if user selects td:
                    elif edit_selection == "td":

                        # request user to input new due date
                        task_date = input("\nPlease enter the new due date for this task in format DD Mon YYYY : \n")

                        # new due date is set to equal -2 index position of task array
                        task_array[-2] = " " + task_date

                        # task array joined together with new due date
                        task_string = ",".join(task_array)

                        # for task in tasks:
                        for task in tasks:

                            # if i is equal to index task number
                            if i == index_task_num:

                                # old due date is replaced with new due date
                                new_line = task.replace(task,task_string)
                            
                            # else old line is kept
                            else:
                                new_line = task

                            # each line is added to replaced_file 
                            replaced_file = replaced_file + new_line

                            # i increased by 1 with each loop
                            i = i + 1
                        
                        # write replaced file to tasks.txt
                        write_file = open("tasks.txt", "w") 
                        write_file.write(replaced_file)
                        write_file.close()

                        # print success message
                        print("\nYour task has been successfully edited")

                # else if user selects c:
                elif edit_task == "c":
                    
                    # indexing used to set final item in task array to yes
                    task_array[-1] = " yes\n" 
                    
                    # task array joined with new edit and converted to string 
                    task_string = ",".join(task_array)
                    
                    # for task in tasks:
                    for task in tasks:

                        # if i equals index task number:
                        if i == index_task_num:

                            # task string with updated due date replaces old string
                            new_line = task.replace(task,task_string)
                        
                        # else old line is kept the same
                        else:
                            new_line = task
                        
                        # each line is added to replaced_file 
                        replaced_file = replaced_file + new_line

                        # i increases by 1 with each loop
                        i = i + 1

                    # write replaced file to tasks.txt
                    write_file = open("tasks.txt", "w") 
                    write_file.write(replaced_file)
                    write_file.close()

                    # print success message
                    print("\nThis task has been marked as complete ")
                        
                # else if user selects -1, exit out of function
                elif edit_task == "-1":
                    return

                # else print incorrect selection, try again
                else:
                    print("\nIncorrect selection, please try again")

            # else print you cannot make changes, task is complete
            else:
                print("\nYou cannot make any changes, this task has already been marked as complete")
        
        # else print invalid entry, try again
        else:
            print("\nInvalid entry, please try viewing your tasks again")

# function which generate reports
def generate_reports():

    # open task_overview_file for writing 
    with open("task_overview.txt", "w", encoding= "utf-8") as task_overview_file:
        
        # open task_file for reading
        task_file = open("tasks.txt", "r")
        tasks = task_file.readlines()

        # variables set to 0, used for keeping count
        no_of_tasks = 0
        completed_tasks = 0
        incomplete_tasks = 0
        overdue_tasks = 0        

        # iterate through each task in tasks.txt and increase number of task by 1
        for task in tasks:

            no_of_tasks = no_of_tasks + 1

            task = (task.split(", "))

            # if final item in task is yes, increase completed_tasks counter by 1
            if task[-1].strip("\n") == "yes":

                completed_tasks = completed_tasks + 1

            # incomplete tasks calculated by subtracting no of tasks by completed tasks
            incomplete_tasks = no_of_tasks - completed_tasks

            # due date extracted from each task and current date set to today's date
            due_date = task[-2]
            current_date = today.strftime('%Y-%m-%d')

            # dates are converted from string format to date format for comparison
            today_date = datetime.strptime(current_date, '%Y-%m-%d').date() 
            due_date = datetime.strptime(due_date, '%d %b %Y').date()

            # if due date has passed the current date and task is not completed, overdue counter increases by 1
            if today_date > due_date and task[-1].strip("\n") == "no":
                overdue_tasks = overdue_tasks + 1
            
            # calaculations to determine percentage of incomplete and overdue tasks
            incomplete_percentage = round((incomplete_tasks / no_of_tasks) * 100, 1)
            overdue_percentage = round((overdue_tasks/no_of_tasks)*100, 1)
    
        # data is written to task_overview file
        task_overview_file.write("TASK OVERVIEW REPORT".center(42, "-") +
        "\n\nTotal tasks:".ljust(39, " ") + str(no_of_tasks) + 
        "\nCompleted tasks:".ljust(38, " ") + str(completed_tasks) +
        "\nIncomplete tasks:".ljust(38, " ") + str(incomplete_tasks)+
        "\nOverdue & incomplete tasks:".ljust(38, " ") + str(overdue_tasks)+ 
        "\nIncomplete perecentage:".ljust(34, " ") + str(incomplete_percentage)+ "%" +
        "\nOverdue percentage:".ljust(34, " ") + str(overdue_percentage) + "%" +
        "\n\n" + "END".center(42, "-"))
    
    # open user_overview_file for writing
    with open("user_overview.txt", "w", encoding= "utf-8") as user_overview_file:

        # open user_file for reading
        user_file = open("user.txt", "r")
        users = user_file.readlines()

        # empty users dictionary to store number of tasks per each user
        usersDictionary = {}

        # iterate through users.txt to access usernames and update dictionary with each username 
        for line in users:

            user = line.split(", ")[0]
            usersDictionary.update({user:0}) 
        
        # number of users equal to length of usersDicitonary
        no_of_users = len(usersDictionary)
        
        # Write titles to user overview file
        user_overview_file.write("USER OVERVIEW REPORT".center(137, "-")+ "\n" +
        "\nTotal users".ljust(39, " ") + str(no_of_users) + 
        "\nTotal tasks generated:".ljust(39, " ") + str(no_of_tasks) + 
        "\n\nUser".ljust(10, " ")+ "Number of tasks assigned".ljust(27, " ") + "% of tasks assigned".ljust(22, " ") +
        "% of completed tasks".ljust(23," ") + "% of incomplete tasks".ljust(24," ") + "% of incomplete & overdue tasks \n\n" )

        # iterates through user in dictionary
        for user in usersDictionary:

            # variables for counting
            completed = 0
            incomplete = 0
            overdue = 0

            # iterates through each task in tasks.txt
            for task in tasks:

                task = task.split(", ")

                # if username is in tasks.txt, user dictionary value for that user incrememnts by 1
                if user == task[0]:                

                    usersDictionary[user] +=1

                    # if task is completed, completed increased by 1
                    if task[-1].strip('\n') == "yes":

                        completed +=1
                    
                    # else increased incomplete counter by 1
                    else:
                        incomplete +=1

                        # today date and due date are converted to dates for comparison
                        today_date = datetime.strptime(current_date, '%Y-%m-%d').date() 
                        due_date = datetime.strptime(task[-2], '%d %b %Y').date()

                        # if due date has passed, increase overdue counter by 1
                        if today_date > due_date:
                            overdue +=1

            # calculate percentage values, round to 1 dp and store as string, if tasks = 0 for user, % is set to 0.0
            percentage_assigned = str(round(((usersDictionary[user]) / no_of_tasks) * 100, 1)) + "%"
            percentage_complete_per_user = str(round((completed / usersDictionary[user]) * 100 if usersDictionary[user] != 0 else 0.0, 1)) + "%"
            percentage_incomplete_per_user = str(round((incomplete  / usersDictionary[user]) * 100 if usersDictionary[user] != 0 else 0.0,1)) + "%"
            percentage_overdue = str(round((overdue/ usersDictionary[user]) * 100 if usersDictionary[user] != 0 else 0.0,1)) + "%"
            
            # write data to user_overview file
            user_overview_file.write(str(user).ljust(20, " ")+ str(usersDictionary[user]).ljust(24, " ")
            + percentage_assigned.ljust(22, " ") + percentage_complete_per_user.ljust(22, " ") + percentage_incomplete_per_user.ljust(29, " ")
            + percentage_overdue + "\n")
        
        # write footer to file
        user_overview_file.write("\n"+ "END".center(137, "-"))

    # close task_file
    task_file.close()

    # print success message
    print("\nTask and user overview reports have been successfully generated.")

# function which displays stats from reports
def display_stats():

    # open tasks_overview.txt in read mode
    with open("task_overview.txt", "r", encoding="utf-8") as task_overview_file:
        
        # iterate through task_overview.txt and print each line
        for line in task_overview_file:
            print(line)

        # add line break at end 
        print("\n")

    # open user_overview.txt in read mode
    with open("user_overview.txt", "r", encoding="utf-8") as user_overview_file:

        # iterate through user_overview.txt and print each line
        for line in user_overview_file:
            print(line)

         # add line break at end 
        print("\n")

# task number is globally assigned to 0, it is used to keep track of task numbers
task_number = 0

# call on user login function through users 
users = user_login()

# while loop to validate login details
while True:

    # request user to enter username and password
    user_name = input("Please enter your username: \n")

    # if user_name is not in dictionary:
    if user_name not in users:

        # print user not found, please try again and restart while loop via continue
        print("\nUser not found please try again!\n")
        continue
    
    # request user for password
    pw = input("Please enter your password \n")

    # else if user name and pw do not match to those in dictionary:
    if users[user_name] != pw:

        # print incorred pw entered for user, try again
        print("\nIncorrect password entered for user, please try again\n")
    
    # else print welcome message and break loop
    else:
        print("\nWelcome, you have successfully logged into your account")
        break 

# while loop presenting menu with different actions
while True:
    
    # assign print_menu function to menu
    menu = print_menu()

    # if r is selected from menu:
    if menu == 'r':
        
        # run add_task function
        reg_user()
            
    # else if d is selected from menu
    elif menu == "ds":

        # run display_stats function
        display_stats()
      
    # else if a is selected from menu:
    elif menu == 'a':

        # run add_task function
        add_task()
    
    # else if va selected from menu:
    elif menu == 'va':
        
        # run view_all function
        view_all(task_number)
    
    # else if vm is selected menu:
    elif menu == 'vm':

        # run view_mine function
        view_mine(task_number)

    # else if gr is selected menu:
    elif menu == "gr":

        # run generate_reports function
        generate_reports()
    
    # else if user selects e from menu:
    elif menu == "e":
        
            # print goodbye and exit
            print('\nGoodbye!!!')
            exit()

    # else print invalid selection
    else:
        print("\nInvalid selection, please try again")

