'''
This week we will create a program that performs file processing activities.
    Your program this week will use the OS library in order to validate that a
directory exists before creating a file in that directory.
    Your program will prompt the user for the directory they would like to save
the file in as well as the name of the file.
    The program should then prompt the user for their name, address, and
phone number. Your program will write this data to a comma separated line in a
file and store the file in the directory specified by the user.

    Once the data has been written your program should read the file you just wrote
to the file system and display the file contents to the user for validation purposes.

Submit a link to your Github repository.

Submission instructions: Click on the title above to submit your assignment.
'''

'''
steps
Startmenu4
    menuprompt asking for directory location choice (3 choices)
    menuprompt runs verify function on directory choice
    verify function returns printout verification of location (represented name,
        not full directory)
    FileEntryFunction Executed, file is created as an empty file with variable name (STR)
    FileLoopEntry executes after that, user enters in all details, each entry being
        a variable.
    Variables written to file, then cleared.
    ReadFunc reads file line by line and prints out the results before initiating
        menuprompt again.



'''
import os
from global_Vars import user_name
from global_Vars import user_address
from global_Vars import user_phonenum
from global_Vars import tree_a1
from global_Vars import tree_a2
from global_Vars import tree_a3
from global_Vars import cwd
from file_Functions import *



menu_start()
