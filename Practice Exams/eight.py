#1 B. oddNumbers[5:]
'''
oddNumbers = [0,1,3,5,7,9,11]

print(oddNumbers[5:15])'''

#2. B age.isalpha()
'''age : int = 23
print(age.isalpha())'''

#3. C.

#4. B.

'''aNumber =5
print(bool(aNumber % 2 == 1))'''

#5. C. def add(o1,o2):

#6. B. aStr += '?'

#7. B, n to the power of n

'''num = 4
mystery = 1
for time in range(num):
    mystery *= num
print(mystery)'''

#8. D; all of the above

#9. C.

'''
var1
var3
var4
'''

#10. F. None of the above

#11. A.

#------------------------------------------------

#Q1
#1. code added for 2 more floors:

'''
# Floor #3
print("\nFloor #3")
aFloor = tilePattern(aWidth, aHeight, "X", "O")
printFloor(aFloor, aHeight)
# Floor #4
print("\nFloor #4")
aFloor = tilePattern(aWidth, aHeight, "-", "~")
printFloor(aFloor, aHeight)
'''

#2.
#   1) print(aFloor) will print out a 2-D array, of the row content in each column [columns[rows]]
#   2) will print out individual lines of the contents of each row as arrays (one line per array)
#   3) printFloor(theFloor, theHeight) will print a joined multiline string, it will look much nicer!

#--------------------------
#Q2

#right after floor 1 code, before floor 2 code ->
'''
aFloor[aHeight//2][aWidth//2] = "MM"

'''
#--------------------------
#Q3
'''
#Places a piece of furniture at a given location on this floor.
def createFloorPlan(theFloor,theFurniture, height, width row, column):
    """Places the furniture height x width @ [column,row], aka 2x6
    """
    for y in range(height):
        for x in range(width):
            theFloor[row][col] = thePattern
            row += 1
        height += 1

'''
#--------------------------
#Q4
'''
file = open("Practice Exams\words.txt","r")
words = file.readlines()

def printLongWords(words):
    for word in words:
        if len(word.strip()) > 20:
            print(word.strip())'''
