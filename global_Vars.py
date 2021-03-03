global user_name
global user_address
global user_phonenum
global tree_a1
global tree_a2
global tree_a3
global user_Choice
global cwd
global wrkFileDirect
import os

#this is our blank variables for the usual information.
user_name = ''
user_address = ''
user_phonenum = ''

tree_a1 = 'location_a/sub_locus_1/locale_a/section_1/'
tree_a2 = 'location_b/sub_locus_1/'
#does not exist, merely a demonstration of error checking/validation
tree_a3 = 'location_c/sub_locus_3/locale_a/not_a_real_directory/'


#this is the variable that decides which directory the user puts his stuff into
user_Choice = ''

#this gets the EXACT directory, from top to bottom.
#thank god for os.path.join, greatest thing I've found.
cwd = os.getcwd()
wrkFileDirect = os.path.join(cwd, user_Choice)
