from global_Vars import user_name
from global_Vars import user_address
from global_Vars import user_phonenum


def menustart():
    print("Welcome to the file program.")
    print("Please type [START] to begin or [QUIT] to end.")
    user_entry = ''
    while user_entry != "END":
        if user_entry == "START":
            menuloop()
            break
        else:
            print("That is not a valid entry, please try again")
            continue
    else:
        quit()

def menuloop()
