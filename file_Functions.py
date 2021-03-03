from global_Vars import user_name
from global_Vars import user_address
from global_Vars import user_phonenum
import os
import sys

#starts the menu, other functions can loop back to here.
def menu_start():
        print("Welcome to the program!")
        print("Type [START] to begin or [QUIT] to end the program.")
        user_entry = "EXCEPTION"
        while user_entry != "QUIT":
            user_entry = input("Enter Command: ")
            if user_entry == "START":
                find_directory()
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
    


#verifies directory existence
def verify_directory(file_directory):
    if os.path.exists(file_directory):
        open_directory()
    else:
        print("directory does not exist, please type the correct directory.")
        choose_directory()






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
