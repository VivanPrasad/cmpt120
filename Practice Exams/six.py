# 1. D
# 2. B
# 3. A
# 4. E
# 5. C

#Q2: False, cannot be rewritten recursively

#Q3: 4 test cases (A)

#Q4
#1a. 1 bit can represent 2 numbers (0, 1)
#1b. 4 bits represents 16 numbers, so 0-15 (0001, 0010... etc)

#2. These numbers range from 0 to (2^7-1) so 2^7 numbers
#3. from 0 to 1 (two numbers) so 2 numbers
#4. from 0 to (2^32-1) numbers, so 2^32 numbers (a lot)

#Q5
#1. 10011011 to decimal = 2^0 + 2^1 + 2^3 + 2^4 + 2^7 = 1 + 2 + 8 + 16 + 128
# = 152 + 3 = 155

#2a. 57/2 = 28r1, 28/2 = 14r0, 14/2 = 7r0, 7/2 = 3r1, 3/2 = 1r1, 1/2 = 0r1.
# read backwards of remainders: 111001
#2b. 157/2 = 78r1, 78/2 = 39r0, 39/2 = 19r1, 19/2 = 9r1, 9/2 = 4r1, 4/2 = 2r0, 2/2 = 1r0, 1/2 = 0r1
# read backwards of remainders: 10011101

#-------------------

#Q1 search_program.py
'''
# returns all the indices where the target can be found 
# in the list (empty if not found)
def linearSearchIndex(searchList:list[int], searchNumber:int) -> list:
    indexes : list[int] = []
    for n in range(len(searchList)):
        if searchList[n] == searchNumber:
            indexes.append(n)
    return indexes

list1 = [10,15,24,15,2]
#test case 1: pick 10 and get [0]
print(linearSearchIndex(list1,10))

#test case 2: pick 15 and get [1,3]
print(linearSearchIndex(list1,15))

#test case2: pick 999 and get []
print(linearSearchIndex(list1,999))'''

#Q2: Vowel Counter

'''
#returns the number of vowels in the string aString using recursion
def countVowels(aString,vowelCount=0):
    #base case, if there are no more items left, just return the current vowels
    if len(aString) < 1:
        return vowelCount
    #add vowelcount if the next letter is in aeiou
    if aString[0].lower() in "aeiou":
        vowelCount += 1
    #recursively return the called countVowels, 
    but removing the 0 index from the string (starting from 1:end)
    return countVowels(aString[1:],vowelCount)

print(countVowels(input("Enter a word to count vowels: ")))'''

#Q3: Decimal to Binary Converter
'''
#converts decimal to binary in python!
def decimalToBinary(decimal:int) -> str:
    remainders = []
    #keep dividing by two
    while decimal > 0:
        remainder = str(decimal % 2)
        remainders.append(remainder)
        decimal //= 2
    #take the remainders (convert to string)
    binaryString = ''.join(remainders[::-1])

    #join remainders into string
    #convert to int
    return binaryString

number = int(input("Enter a base 10 number to convert to binary: "))
print(f'The binary version of {number} = {decimalToBinary(number)}')'''