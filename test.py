# path: test.py
# prompts the user for username and password, and checks if the username and password are valid.
# The password is valid if it is at least 8 characters long and has at least one uppercase letter, one lowercase letter, and one number.
# If the username and password are valid, return True. Otherwise, return False.
# Use regular expressions to validate the username and password.
# import the regex module
import re
# Write the regex
regex = r"[A-Za-z0-9]{8,}"
#loop until the user enters a valid username
username = input("Enter username: ")
while not re.search(regex, username):
    print("Invalid username. Try again.")
    username = input("Enter username: ")
   
#compile the regex
pattern = re.compile(regex)
password = input("Enter password: ")
# Find all matches of regex in input
if re.search(pattern, password):
    print("Password is valid.")
else:
    print("Password is invalid.")

    