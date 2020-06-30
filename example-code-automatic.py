# scrap requires a total of three lines of python code for you to use
# this example shows how scrap can be called automatically to direct all print() commands ...
# ... and all error output to your scrap
# this is great if you don't have access to 

import scrap  # this needs to be done on every script you write to a scrap from


### Link this folder to a scrap key
# This command only needs to be invoked once for each project directory you work in - it will save the key to a file for use going forward
# but there's no harm in running it each time if you prefer - it will overwrite nicely
scrap.setup("scrap-testing")


### Show how we can redirect all print output to scrap
print ("This will print to your screen ...)

scrap.auto_scrap_on_print()  #Set up scrap to automatically capture all print()

print ("... but now this will show on your scrap")
print ("as will this")
print ("and any future output you send to print()")


### Show how we can redirect all error output to scrap

scrap.auto_scrap_on_error()  #Set up scrap to automatically capture all print()

# Trying to divide by zero will result in an error
a = 1 / 0

# ... which will show up on your scrap