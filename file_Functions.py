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
    #the usual menu loop
    while user_entry != "QUIT":
        user_entry = input("Enter Command: ")
        if user_entry == "START":
            #choosing the directory and the starting the function chain
            choose_directory()
            break
        elif user_entry == "QUIT":
            #different quitting method
            #Still haven't figured out why it's giving out like it is.
            #quit() gives an error, even though it ends the program...
            systemshutdown()
            #sys.exit(0)
            break
        else:
            print("That is not a valid entry.\nPlease try again.")
            continue


#lets the user type in the directory choice
def choose_directory():
    user_entry = "EXCEPTION"
    #could not get user entry to become or call variable name...dictionary might
    #work but that's just more effort.
    while user_entry != "QUIT":
        print("Please choose one of three directories listed:")
        print("Directory [tree_a1]")
        print("Directory [tree_a2]")
        print("Directory [tree_a3]")
        user_entry = input("Please enter: ")
        wrkFileDirect = '' #this guy right here is the working file directory plus
        #whatever else is appended to it. To put it simply, he's going to be our
        #full branch from top to the chosen bottom, passed through almost every
        #function, hence why despite being a local variable as opposed to global,
        #he's called the same name everywhere.
        if user_entry == "tree_a1":
            #assinging the global variable
            user_Choice = tree_a1
            wrkFileDirect = os.path.join(cwd, user_Choice)
            verify_directory(wrkFileDirect)
            break
        elif user_entry == "tree_a2":
            user_Choice = tree_a2
            wrkFileDirect = os.path.join(cwd, user_Choice)
            verify_directory(wrkFileDirect)
            break
            #tree_a3 does NOT exist, merely a demonstration that the directory
            #verification system works.
        elif user_entry == "tree_a3":
            user_Choice = tree_a3
            wrkFileDirect = os.path.join(cwd, user_Choice)
            verify_directory(wrkFileDirect)
            break
        else:
            print("Not a valid entry, try again.")
            continue


#verifies directory existence
def verify_directory(file_directory):
    print("Directory is listed as:\n")
    print(file_directory)
    if os.path.exists(file_directory):
        print("Directory does exist, proceeding...")
        details_entry(file_directory)
    else:
        #bounces us back to the menu again
        print("Directory does not exist, please choose a different directory.")
        choose_directory()

#user enters in details to be written to the file.
def details_entry(wrkFileDirect):
    print('''Please enter the specified information below for each prompt: \n
    Filename, name, address, and phone number.
    ''')
    print("Please enter your desired filename.")
    file_name = input("Filename: ")
    print("User entry is: ", file_name)
    print("Please enter your name.")
    user_name = input("Name: ")
    print("User entry is: ", user_name)
    print("Please enter your address.")
    user_address = input("Address: ")
    print("User entry is: ", user_address)
    print("Please enter your phone number.")
    user_phonenum = input("Phone Number: ")
    print("User entry is: ", user_phonenum)
    #writes each variable to the file, but also passes each variable to the display
    #output.
    writeXread_data(file_name, user_name, user_address, user_phonenum, wrkFileDirect)

#this writes the chosen data to the chosen file location(user choice)
def writeXread_data(filename, username, u_address, u_number, wrkFileDirect):
    #gotta love path.join
    #wrkFileDirect, from beginning to end.
    action = open(os.path.join(wrkFileDirect, filename), "w+")
    action.write("Name: " + username + "\n")
    action.write("Address: " + u_address + "\n")
    action.write("Phone Number" + su_number + "\n")
    action.close()
    #I tried to get the program to both write the info and read it in one go,
    #but something wasn't working properly. Could you point out what I was doing wrong?
    action2 = open(os.path.join(wrkFileDirect, filename), "r")
    READCONTENTS = action2.read()
    print(READCONTENTS)
    #action2.seek(0)
    action2.close()
    menu_start()

def systemshutdown():
    print("Thank you for using the program, have a wonderful day!")
