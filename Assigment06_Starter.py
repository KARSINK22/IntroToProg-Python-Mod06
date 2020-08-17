# ---------------------------------------------------------------------------- #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added code to complete assignment 5
# K. Sinkevitch,8/15/20,Modified code to complete assignment 6
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
strFileName = "ToDoFile.txt"  # The name of the data file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strChoice = ""  # Captures the user option selection
strTask = ""  # Captures the user task data
strPriority = ""  # Captures the user priority data
strStatus = ""  # Captures the status of processing functions


# Processing  --------------------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        list_of_rows.clear()  # clear current data
        file = open(file_name, "r")
        for line in file:
            task, priority = line.split(",")
            row = {"Task": task.strip(), "Priority": priority.strip()}
            list_of_rows.append(row)
        file.close()
        return list_of_rows, 'Success'

    @staticmethod
    def add_data_to_list(task, priority, list_of_rows):
        # TODO: Add Code Here!
        """ Adds a row of data in a list of dictionary rows

        :param task: (string) description of task:
        :param priority: (string) priority of the task:
        :param list_of_rows: (list) you want to add the data to:
        :return: (string) status message
        """
        row = {"Task": task.strip(), "Priority": priority.strip()}  # Create new row of data with passed values
        list_of_rows.append(row)  # Add the row to the list
        return 'Success'

    @staticmethod
    def remove_data_from_list(task, list_of_rows):
        # TODO: Add Code Here!
        """ Removes a row of data in a list of dictionary rows

        :param task: (string) description of task:
        :param list_of_rows: (list) you want to remove data from:
        :return: (list) of dictionary rows, (string) status message
        """
        lstOfItemsKept = []  # Initialize new list of items to be kept
        strMsg = "Item not found"  # Initialize return message

        for row in list_of_rows:  # For every row in the list, only copy the rows to be kept into new list
            if row["Task"].lower() != task.lower():  # Check if the row's Task value is not equal to the value to delete
                lstOfItemsKept.append(row)  # Create new list of rows that should be kept
            else:
                strMsg = 'Success'  # Value is found and not added to new list (i.e., deleted)
        list_of_rows = lstOfItemsKept  # Set list_of_rows address to the new list of items to keep
        return list_of_rows, strMsg

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        # TODO: Add Code Here!
        """ Writes list of dictionary rows to a file

        :param file_name: (string) name of file:
        :param list_of_rows: (list) you want to add the data to:
        :return: (string) status message
        """
        try:  # Use try-except block to make sure file can be opened without error
            objFile = open(file_name, "w")  # Open file
            for row in list_of_rows:  # for each row (dictionary) in list, write to file
                objFile.write(str(row["Task"]) + "," + str(row["Priority"]) + "\n")
            objFile.close()  # Close file
            return 'Success'
        except:
            return 'Sorry, not able to save your data'


# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def print_menu_Tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new Task
        2) Remove an existing Task
        3) Save Data to File        
        4) Reload Data from File
        5) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_Tasks_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current Tasks ToDo are: *******")
        for row in list_of_rows:
            print(row["Task"] + " (" + row["Priority"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user

        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_new_task_and_priority():
        """ Input a new task and priority

        :param:  none
        :return: (string) task, (string) priority
        """
        # TODO: Add Code Here!
        task = input(" Enter a new task: ")  # Prompt user for new task description
        priority = input(" Enter the task's priority: ")  # Prompt user for new task's priority
        return task, priority

    @staticmethod
    def input_task_to_remove():
        """ Input a task to remove from list

        :param:  none
        :return: (string) task
        """
        # TODO: Add Code Here!
        task = input(" Enter task to remove from list: ")  # Prompt user for task to remove
        return task


# Main Body of Script  ------------------------------------------------------ #

# Step 1 - When the program starts, Load data from ToDoFile.txt.
Processor.read_data_from_file(strFileName, lstTable)  # Read file data

# Step 2 - Display a menu of choices to the user
while True:
    # Step 3 Show current data
    IO.print_current_Tasks_in_list(lstTable)  # Show current data in the list/table
    IO.print_menu_Tasks()  # Shows menu
    strChoice = IO.input_menu_choice()  # Get menu option

    # Step 4 - Process user's menu choice
    if strChoice.strip() == '1':  # Add a new Task
        # TODO: Add Code Here
        strTask, strPriority = IO.input_new_task_and_priority()  # Get task and priority to add to list
        strStatus = Processor.add_data_to_list(strTask, strPriority, lstTable)  # Add new task to list
        IO.input_press_to_continue(strStatus)  # Provide status message
        continue  # To show the menu

    elif strChoice == '2':  # Remove an existing Task
        # TODO: Add Code Here
        strTask = IO.input_task_to_remove()  # Get task to remove from list
        lstTable, strStatus = Processor.remove_data_from_list(strTask, lstTable)  # Remove task from list
        IO.input_press_to_continue(strStatus)  # Provide status message
        continue  # To show the menu

    elif strChoice == '3':  # Save Data to File
        strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")  # Verify user wants to save to file
        if strChoice.lower() == "y":
            # TODO: Add Code Here!
            strStatus = Processor.write_data_to_file(strFileName, lstTable)  # Save data to file
            IO.input_press_to_continue(strStatus)  # Provide status message
        else:
            IO.input_press_to_continue("Save Cancelled!")  # Provide status message
        continue  # To show the menu

    elif strChoice == '4':  # Reload Data from File
        print("Warning: Unsaved Data Will Be Lost!")
        strChoice = IO.input_yes_no_choice("Are you sure you want to reload data from file? (y/n) -  ")
        if strChoice.lower() == 'y':
            # TODO: Add Code Here!
            Processor.read_data_from_file(strFileName, lstTable)  # Read data from file
            IO.input_press_to_continue(strStatus)  # Provide status message
        else:
            IO.input_press_to_continue("File Reload  Cancelled!")  # Provide status message
        continue  # to show the menu

    elif strChoice == '5':  # Exit Program
        print("Goodbye!")
        break  # Exit
