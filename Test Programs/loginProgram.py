# loginProgram.py
#
# Description: Allows the user to login with a password
#
# Author: M. Vivan Prasad
# Date: W Sept. 13, 2023

accounts = {
    "admin":"1234"}

username = input("Please Enter Username")
password = input("Please Enter Password")

while not username in accounts.keys() or password in accounts.values():
    print("Invalid username or password")
    username = input("Enter Username")
    password = input("Enter Password")


print(f"Welcome, {username}!")
