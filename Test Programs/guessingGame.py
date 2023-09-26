# guessingGame.py
#
# Description: A game where the user has to guess the number
# is 'thinking' of LMAOOO
#
# Author: M. Vivan Prasad
#
# Date: Monday September 18th, 2023

import random
from random import randint as rand_int

def game():
    computerNumber = rand_int(1,10)
    userNumber = input("Guess my number from 1 to 10 :}\n").strip()
    while not userNumber.isnumeric() and not userNumber in range(1,11):
        userNumber = input("Must be a number from 1 to 10 and a valid number! Guess again: \n")
    if int(userNumber) == computerNumber:
        print("Gah! You got me :(")
    else:
        print("Nice try! Muahahaha")
    retry()

def retry():
    response = input("Play again? (Y/N)\n").lower().strip()
    if response == "y":
        game()