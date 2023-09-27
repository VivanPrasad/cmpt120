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
positiveWords = [
    "awesome","great","good","happy","ok","okay",
    "well","amazing","splendid","estatic","excited"]
negativeWords = [
    "bad","horrible","tired","sleepy","sad","sick",
    "unwell","worried","stressed","scared","overwhelmed"]

#A list of the chatbot responses based on the scenario
chatbotResponses = [
    "I see...",
    "That's good to hear :)",
    "Oh... sorry about that. I hope everything works out in the end!",
    "Okay..."]

#The chatbot, Sora from Kingdom Hearts, greets himself.
#He is very loud and outgoing, and I tried to make the chatbot enthusiastic
print("Hello! The name's Sora, from Kingdom Hearts!")

#Asks the user how they are doing
userResponse = input("How ya doin'?\n").lower()

#removes punctuation from the user's response
for punctuation in "?!,.-":
    userResponse = userResponse.replace(punctuation,"")

#Splits the user's words into a list to be analyzed
splitUserResponse = userResponse.split(" ")

#A variable to check which response the chatbot should put out
responseType = 0
#Check each word in the positiveWords list (check above)
for word in positiveWords:
    #If a positive word is in the list of words from the splitUserResponse,
    #then increment the responseType by 1 and break the for loop
    if word in splitUserResponse:
        responseType += 1
        break
for word in negativeWords:
    #If a negative word is in the list of words from the splitUserResponse, 
    #then increment the responseType by 2 and break the for loop
    if word in splitUserResponse:
        responseType += 2
        break

#Prints the message from the list, with the index of the response type
#0: Unknown response (no words both positive or negative were found)
#1: Positive response (a positive word was found in the user's response)
#2: Negative response (a negative word was found in the user's response)
#3: Mixed response (1+2) (both a positive word and negative word were found)
print(chatbotResponses[responseType])

#Gets the name of the user in lowercase and stripped
userName = input("What is your name?\n").lower()
print(f"Hello, {userName.title()}!")

#Gets the user's favourite color
favoriteColor = input("There are infinite things to talk about,\n\
so I'll just start simple. What's your favorite color?\n").lower()

#Splits the user's response of their favorite color into separate words
splitFavoriteColor = favoriteColor.split(" ")

#Prints "I like that color too!" when the word "purple" or 
#"pink" is in the list of words they inputted
if "purple" in splitFavoriteColor or "pink" in splitFavoriteColor:
    print("I like that color too! My favourite color is blue :)")
#Prints "Blue is my favorite color too!" when 
#blue is found inside the list of words the user said
elif "blue" in splitFavoriteColor:
    print("No way! Blue is my favorite color too!")
#Prints "Awesome!" when any other color is inputted
#(AKA when no blue pink or purple is detected)
else:
    print("Awesome!")

#Asks the user for their favourite food, lowercases it
#and stores it in the variable "favoriteFood"
favouriteFood = input(
    "Let's talk about food! What type of food do you like to eat?\n").lower()

#Splits the sentence of the user into words in the variable 
#splitFavouriteFood, which allows each word to be analyzed
splitFavouriteFood = favouriteFood.split(" ")

#Prints "Pizza is so good!" if the word "pizza" is in 
#the list of words from the favoriteFood input
if "pizza" in splitFavouriteFood:
    print("Pizza is so good!")

#Prints "Pasta is quite yummy!" if the word "pasta" is in the
#list of words in the splitFavoriteFood variable
#Then prints "Just thinking baout food is making me hungry!"
#after the previous statement is printed out
if "pasta" in splitFavouriteFood:
    print("Pasta is quite yummy if I say so myself!")
    print("Just thinking about food is making me hungry!")
#Prints "I should try it sometime... oh wait I can't..."
#when the word "pasta" is not found in the sentence.
#This automatically prints whether pizza is found as well,
#to add more variety to the conversation.
else:
    print("I should try it sometime... oh wait I can't...")

#Says goodbye to the user as the final output and program ends
print(f"Well, it was nice to meet you {userName.capitalize()}!\n\
I hope we can meet again sometime.\n\
I have to go find my friends, Riku and Kairi!\n\
See ya later!")