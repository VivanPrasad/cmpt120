# chatbotTest.py
#
# greetingsWithNameAndBandWithRandomness
# 
# Author: M. Vivan Prasad
# Date: Mon Sept. 11, 2023
# 

import random

# Greet the user and get the user's name
name = input("Hi!, What is your name?\n")

# Respond "Nice to meet you, <user's name>!"
print(f"Nice to meet you, {name}!")

#Ask and get the person's your favourite band is
favouriteBand = input("What is your favourite band?\n")

bandComments = [
    f"{favouriteBand} is a cool band!",
    "Mine too!",
    "Cool!",
    f"Oh. I don't know {favouriteBand}."]

#Get the random comment from the bandComments list
randomComment = random.choice(bandComments)

#Make a random comment of the person's response
print(randomComment)

#Print random fortune cookie statements
