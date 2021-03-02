from global_Vars import user_name
from global_Vars import user_address
from global_Vars import user_phonenum

import sys

def menu_start():
        print("Welcome to the program!")
        print("Type [START] to begin or [QUIT] to end the program.")
        user_entry = ''
        while user_entry != "QUIT":
            user_entry = input("Enter Command: ")
            if user_entry == "NEXT":
                menuloop()
                break
            elif user_entry == "QUIT":
                print("Thank you for using the virtual garage!")
                sys.exit(["User has chosen to quit.\nThe program will now end."])
                break
            else:
                print("That is not a valid entry.\nPlease try again.")
                continue

#def menuloop()
