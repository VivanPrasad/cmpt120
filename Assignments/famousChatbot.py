# famousChatbot.py
#
# Description: Create a Famous Personality chatbot
#
# Author: M. Vivan Prasad
#
# Date Created: Monday September 18th, 2023
# Last Updated: Wednesday September 27th, 2023

#Criteria
#whether your program executes (e.g., does it contain any errors) (5 points)
#whether your program solves the problem (5 points).

import random, time, math

#A list of positive words that the user may input for greeting
positiveWords = ["awesome","great","good","great","happy","ok","okay","well"]
negativeWords = ["bad","horrible","tired","sleepy","sad","sick","unwell"]

#A list of the chatbot responses based on the scenario
chatbotResponses = [
    "I see...",
    "That's good to hear :)",
    "Sorry to hear that :(",
    "Okay..."]

#Asks the user how they are doing (ensure no punctuation)
userResponse = input("Greetings! How are you?\n").lower()

#Removes punctuation from the user response
for punctuationMark in ",.!?-":
    userResponse.replace(punctuationMark,"")

#Splits the user's words into a list to be analyzed
splitUserResponse = userResponse.split(" ")


#A variable to check which response the chatbot should put out
responseType = 0
#Check each word in the response
for word in splitUserResponse:
    #If a word is in the positiveWords list, then add 1 to the response type
    if word in positiveWords:
        responseType += 1
        
    elif word in negativeWords:
        responseType += 2

#Prints the message from the list, with the index of the response type
#0: Unknown response
#1: Positive response
#2: Negative response
#3: Mixed response (1+2)
print(chatbotResponses[responseType])

#Gets the name of the user in lowercase and stripped
name = input("What is your name?\n").lower()
print(f"Hello, {name.title()}!")

#Gets the user's favourite color
favoriteColor = input("What is your favorite color\n").lower()

#Prints "I like that color too!" when the user inputs purple or pink
if favoriteColor in ["purple","pink"]:
    print("I like that color too!")
#Prints "Blue is my favorite color too!" when the user inputs blue
elif favoriteColor == "blue":
    print("Blue is my favorite color too!")
#Prints "Awesome!" when any other color is inputted
else:
    print("Awesome!")

favouriteFood = input("What type of food do you like to eat?\n").lower().split(" ")

if "pizza" in favouriteFood:
    print(f"{' '.join(favouriteFood).capitalize()} is so good!")

if "pasta" in favouriteFood:
    print("Pasta is yummy!")
else:
    print("Sounds good! I should try it sometime... oh wait I can't...")