# ROT13_Solver.py
#
# Description: Write a program that encrypts and decrypts strings using ROT13
#
# Author: M. Vivan Prasad
#
# Date Created: Monday October 9th, 2023
# Last Updated: Wednesday October 11th, 2023

#A string of all the lowercase alphabet, used to shift letters for the cypher
alphabet : str = "abcdefghijklmnopqrstuvwxyz"

#A function to shift individual letters, to filter if it is in the alphabet,
#and if the letter is uppercase or lowercase.
def translate_letter(letter : str) -> str:
    #checks if the letter is uppercase (will be used leter)
    letterIsUppercase = bool(letter.isupper())
    #makes the letter lowercase so that if it is alphabetic, it
    #can be found in the alphabet list
    letter = letter.lower()
    #Checks if the letter is alphabetic, else just return the same letter
    if letter.isalpha():
        #Gets the index in the alphabet in which the new letter should be
        #after shifting it 13 to the right (using modulus to wrap around)
        new_index = (alphabet.find(letter) + 13) % len(alphabet)
        #Get the letter from the newly identified index
        new_letter = alphabet[new_index]

        #If the letter was uppercase, remake it as uppercase
        if letterIsUppercase:
            new_letter = new_letter.upper()
    else:
        #If the letter is not alphabetic (a symbol or number), return
        #the same letter, ignoring the encryption
        new_letter = letter
    return new_letter

#A function to put through the user's message through the ROT13 algorithm
def encrypt(message : str) -> str:
    #start with an empty string
    encrypted_message = ""

    #For each letter in the user's message
    for letter in message:
        #Check if the letter is uppercased
        #Add the returned translated letter to the message 
        encrypted_message = encrypted_message + translate_letter(letter)
    #returns the newly encrypted message
    return encrypted_message

def decrypt(message : str) -> str:
    '''The decryption of ROT13 is an inverse and "undos" 
    itself, so putting it through encryption twice would 
    result  in the same output as the the input'''
    #return the double encrypted message (which undos its encryption)
    return encrypt(encrypt(message))

#Asks the user for their initial input
user_input : str = input("Please, enter a message to encrypt/decrypt or \
enter an empty string to exit the program:\n>")
# MAIN LOOP (repeats until the user enters an empty string to exit the loop)
while user_input != "":
    #Prints out the original message, the encrypted message and
    #the decrypted message run twice through the ROT13 algorithm
    print(f"Original: {user_input}")
    print(f"Encrypted: {encrypt(user_input)}")
    print(f"Decrypted: {decrypt(user_input)}")
    #Ask the user again, and keep asking until the while loop becomes false
    user_input = input("Please, enter a message to encrypt/decrypt \
or enter an empty string to exit the program:\n>")
