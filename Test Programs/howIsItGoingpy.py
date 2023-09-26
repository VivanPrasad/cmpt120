# howIsItGoing.py
#
# Description: Make a chatbot that asks a user how their
# day is going, and make a comment that
# changes depending on how the user answered
#
# Author: M. Vivan Prasad
# Date: W Sept. 13, 2023

response = input("Hey! How is it going?\n").lower().strip()

goodWords = ["good","great","awesome","splendid","amazing"]
badWords = ["worried","bad","not good"]


def analyze_response():
    responseWords = response.split(" ")
    print(f"Good Word: {[x for x in responseWords if x in goodWords]}")
    print(f"Negative Word: {[x for x in responseWords if x in badWords]}")
    # If user says "Awesome!", reply "Good to hear!"
    if response in ["awesome!", "good!"]:
        print("Great to hear!")
    #"If user says "Bad!", reply "Sorry to hear!"
    elif response in ["bad!", "horrible!"]:
        print("Sorry to hear!")
    #For all other responses, reply "Oh! I see...!"
    else:
        print("Oh! I see...!")

    print("What are you up to today?")

analyze_response()
