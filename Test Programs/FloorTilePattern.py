# FloorTilePattern.py
#
# Description: Creates and displays a floor tile pattern.
#
# Author: AL
# Date: Dec. 2023

# -------------------------------------------------------------------

def tilePattern(theWidth, theHeight, noPattern, thePattern):
    ''' Producesa floor tile pattern composed of 2 characters
        (2 characters per cell), saves it in the variable "theFloor"
        of "theWidth" by "theHeight" and returns it. 

        Requirement: Each of the "theHeight" rows contains 2 x "theWidth"
                     characters and is one character high. '''

    # Create the two-character cell pattern 
    pattern = noPattern + thePattern

    # Create the floor tile pattern of "theWidth" by "theHeight"
    theFloor = [[(pattern) for i in range(theWidth)] for j in range(theHeight)]

    return theFloor

# -------------------------------------------------------------------

def printFloor(theFloor, theHeight):
    ''' Print the floor. '''
    
    for row in range(theHeight):
        # print(theFloor[row]) 
        aRow = "".join(theFloor[row])
        print(aRow)
        
    return

# -------------------------------------------------------------------
def createFloorPlan(theFloor,theFurniture, width, height, row, column):
    """Places the furniture height x width @ [column,row], aka 2x6
    """
    for y in range(height):
        theFloor[row][column] = theFurniture
        row += 1
    
    return theFloor
#*** Main part of the program
aHeight = 10
aWidth = 10

# Floor #1
print("\nFloor #1")
aFloor = tilePattern(aWidth, aHeight, "1", "O")
aFloor[(aHeight-1)//2][(aWidth-1)//2] = "MM"
printFloor(aFloor, aHeight)
# Floor #2
print("\nFloor #2")
aFloor = tilePattern(aWidth, aHeight, "*", "O")
printFloor(aFloor, aHeight)

print("\nFloor Plan")
sofa = 'SS'
floorPlan = tilePattern(aWidth, aHeight, "^", "-")
floorPlan = createFloorPlan(aFloor,sofa,2,6,1,9)
printFloor(floorPlan,aHeight)

