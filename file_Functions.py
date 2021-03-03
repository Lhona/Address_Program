from global_Vars import user_name
from global_Vars import user_address
from global_Vars import user_phonenum
from global_Vars import tree_a1
from global_Vars import tree_a2
from global_Vars import tree_a3
from global_Vars import cwd

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
            choose_directory()
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
        wrkFileDirect = ''
        if user_entry == "tree_a1":
            #assinging the global variable
            user_Choice = tree_a1
            wrkFileDirect = os.path.join(cwd, user_Choice)
            verify_directory(wrkFileDirect)
            print("Directory is listed as:\n")
            print(wrkFileDirect)

            break
        elif user_entry == "tree_a2":
            user_Choice = tree_a2
            wrkFileDirect = os.path.join(cwd, user_Choice)
            verify_directory(wrkFileDirect)
            print("Directory is listed as:\n")
            print(wrkFileDirect)
            break
            #tree_a3 does NOT exist, merely a demonstration that the directory
            #verification system works.
        elif user_entry == "tree_a3":
            user_Choice = tree_a3
            wrkFileDirect = os.path.join(cwd, user_Choice)
            verify_directory(wrkFileDirect)
            print("Directory is listed as:\n")
            print(wrkFileDirect)
            break
        else:
            print("Not a valid entry, try again.")
            continue


#verifies directory existence
def verify_directory(file_directory):
    if os.path.exists(file_directory):
        print("Directory does exist, proceeding...")
        details_entry(file_directory)
    else:
        print("Directory does not exist, please choose a different directory.")
        choose_directory()

#user enters in details to be written to the file.
def details_entry(wrkFileDirect):
    print('''Please enter the specified information below for each prompt: \n
    Filename, name, address, and phone number.
    ''')
    print("Please enter your desired filename.")
    file_name = input("Filename: ")
    create = open(os.path.join(wrkFileDirect, file_name), "x")
    print("Please enter your name.")
    user_name = input("Name: ")
    print("Please enter your address.")
    user_address = input("Address: ")
    print("Please enter your phone number.")
    user_phonenum = input("Phone Number: ")
    writeXread_data(file_name, user_name, user_address, user_phonenum, wrkFileDirect)

#this writes the chosen data to the chosen file location(user choice)
def writeXread_data(filename, username, u_address, u_number, wrkFileDirect):
    action = open(os.path.join(wrkFileDirect, filename), "w")
    action.write(username + "\n")
    action.write(u_address + "\n")
    action.write(u_number + "\n")
    action.close()

    TYPE = open(os.path.join(wrkFileDirect, filename), "r")
    READCONTENTS = TYPE.read()
    print(READCONTENTS)
    TYPE.close()
