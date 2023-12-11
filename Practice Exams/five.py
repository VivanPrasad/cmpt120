# recursiveStars.py
#
# Description: Recursively prints out stars

# Name: M. Vivan Prasad
# Date: Sunday December 12, 2023
'''
def printStars(number):
    if number == 0:
        return
    stars_row = '*' * number
    print(stars_row)
    printStars(number-1)

    stars_row = '*' * number
    print(stars_row)

user_input = int(input("Please, enter the number of stars to print: "))
printStars(user_input)'''
'''
def reverseString(string) -> str:
    if len(string) < 1:
        return string
    return reverseString(string[1:])+string[0]
user = input("")
string = reverseString(user)
print(string)'''

hello = range(10)
print(hello[-2])