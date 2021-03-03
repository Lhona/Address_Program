from global_Vars import user_name
from global_Vars import user_address
from global_Vars import user_phonenum
from global_Vars import tree_a1
from global_Vars import tree_a2
from global_Vars import tree_a3
import os
import sys

#choose directory
#verify directory
#enter data + filename
#write data + filename(essentially creating it)
#read file
#print file contents



#starts the menu, other functions can loop back to here.
def menu_start():
    print("Welcome to the program!")
    print("Type [START] to begin or [QUIT] to end the program.")
    user_entry = "EXCEPTION"
    while user_entry != "QUIT":
        user_entry = input("Enter Command: ")
        if user_entry == "START":
            data_entry()
            break
        elif user_entry == "QUIT":
            print("Thank you for using the program!")
            #different quitting method
            sys.exit(["User has chosen to quit.The program will now end."])
            break
        else:
            print("That is not a valid entry.\nPlease try again.")
            continue


#lets the user type in the directory choice
def choose_directory():
    user_entry = "EXCEPTION"
    while user_entry != "QUIT":
        print("Please choose one of three directories listed:")
        print("Directory [tree_a1]")
        print("Directory [tree_a2]")
        print("Directory [tree_a3]")
        user_entry = input("Please enter: ")
        if user_entry == "tree_a1":
            verify_directory(user_entry)
            break
        elif user_entry == "tree_a2":
            verify_directory(user_entry)
            break
        elif user_entry == "tree_a3":
            verify_directory(user_entry)
            break
        else:
            print("Not a valid entry, try again.")
            continue


#verifies directory existence
def verify_directory(file_directory):
    if os.path.exists(file_directory):
        open_directory()
    else:
        print("directory does not exist, please type the correct directory.")
        choose_directory()

#user enters in details to be written to the file.
def details_entry():
    print('''Please enter the specified information below for each prompt: \n
    Name, address, and phone number.
    ''')
    print("Please enter your name.")
    user_name = input("Name: ")
    print("Please enter your address.")
    user_address = input("Address: ")
    print("Please enter your phone number.")
    user_phonenum = input("Phone Number: ")
