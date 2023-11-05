# MyMarioGame_A4.py
# 
# Description: Set up the Mario game by reading data from the input data file
#              and using this data to initialize variables, then create and
#              display the maze in which Mario is to move.
#
# Please, read Readings 12.1 to 12.5 (inclusively) as well as 
# 11.1 to 11.5 (inclusively). Also, read about Python lists of lists.
#
# Author: AL + MVP
# Credit: Incomplete MyMarioGame_A4.py by AL
# Date Created: Nov. 5 2023
# Date Updated:

# -------------------------------------------------------------------

def createMaze(aMaze, aWidth, aHeight, aCell):
    ''' Create and return "aMaze" of "aWidth" by "aHeight".
        Each cell of the maze is a string set to "aCell".      
    '''
    aMaze = [ [ (aCell) for i in range(aWidth) ] for j in range(aHeight) ]
    
    return aMaze

# -------------------------------------------------------------------

# Print Maze - This function is to used for testing and debugging purposes only!
def printMaze(aMaze, aHeight):
    ''' Print "aMaze" of "aHeight" - for testing and debugging purposes.
    ''' 
    for row in range(aHeight):
        print(aMaze[row])  
    return
		
# -------------------------------------------------------------------

def createBoundaryList(aWidth, bH = "---"):
    ''' Create and return a list that contains 2 lists: the first list
        is the top boundary of the maze and contains a string set to "bH".
        The second list is the bottom boundary of the maze and it also
        contains a string set to "bH".

        Other parameter:
         "aWidth" is the width of the maze.
    '''
    return list([[(bH) for number in range(aWidth)],
                 [(bH) for number in range(aWidth)]])                

# -------------------------------------------------------------------

def displayMaze(aMaze, aWidth, aHeight, hBoundary, bS = "|" ):
    ''' Display "aMaze" with column numbers at the top and row numbers
        to the left of each row along with the top and the bottom boundaries
        "hBoundary" that surround the maze.

        Other parameters:
         "aWidth" is the width of the maze.
         "aHeight" is the height of the maze.
         "bS" is the symbol used for the vertical border.
    '''
    
    offset = 3
    aString = (offset+1) * " "

    print()  
    # Display a row of numbers from 1 to aWidth
    for column in range(aWidth):
        aString = aString + str(column+1) + " "
        if len(str(column+1)) == 1 :
            aString += " "           
    print(aString)

    # Display the top boundary of maze
    print(offset * " " + "".join(hBoundary[0])) 
    
    # Display a column of numbers from 1 to aHeight
    # + left and right boundaries of the maze
    for row in range(aHeight):
        pre = str(row+1) + " " + bS

        # If the displayed row number is >= 10 - adjusting for extra digit
        if row >= 9: # Here 9 since we start at 0
           pre = str(row+1) + bS

        post = bS
        aRow = pre + ''.join(aMaze[row]) + post
        print(aRow)

    # Display the bottom boundary of maze
    print(offset * " " + "".join(hBoundary[1]))
    
    return

# -------------------------------------------------------------------

def placeExitGate(aWidth, aHeight, rowMario, columnMario, hBoundary,
                  exitGate = " = "):
    ''' Place the "exitGate" at the opposite corner of Mario's location.
	In other words, place the "exitGate" either in the top boundary or 
	in the bottom boundary whichever is at the opposite corner of
	Mario's location at coordinates ("columnMario","rowMario").

        Other parameters:
         "aWidth" is the width of the maze.
         "aHeight" is the height of the maze.
         "hBoundary" is a list of 2 lists: the first list is the top boundary
                                   and the second list is the bottom boundary.

        Returned value:
         "hBoundary" updated.
         "exitGateLocationList" contains coordinates x and y of the "exitgate".
    '''
    
    exitGateRight = False
    exitGateBottom = False

    # Create "exitGateLocationList" with initial location of "exitGate"
    # at the top left of maze
    exitGateLocationList.insert(0, 0)   
    exitGateLocationList.insert(1, 0)
    
    # Where is Mario?
    # If Mario is top left then exit gate is bottom right
    if columnMario <= ((aWidth) // 2) : # Mario on the left?
        exitGateLocationList[1] = aWidth - 1  # Yes, then "exitGate" on right
        exitGateRight = True
    # No, then assuption holds -> exit gate on the left
    if rowMario <= ((aHeight) // 2) :   # Mario at the top?
        exitGateLocationList[0] = aHeight - 1  # Yes, then "exitGate" at bottom
        exitGateBottom = True
        # No, then initial position of "exitGate" holds at the top left of maze

    # Place "exitGate" in appropriate top/bottom boundary
    if exitGateBottom :
        del hBoundary[1][exitGateLocationList[1]]
        hBoundary[1].insert(exitGateLocationList[1], exitGate)
    else:
        del hBoundary[0][exitGateLocationList[1]]
        hBoundary[0].insert(exitGateLocationList[1], exitGate)       

    # Can return a tuple -> elements sepatared by a coma
    return hBoundary, exitGateLocationList  

# -------------------------------------------------------------------


# ***Main part of the program

# Welcome the user and identify the game
print("""Welcome to my Mario game.\n""")

# Ask user for filename
filename = input("Please, enter a filename: ")

# Open file for reading
file = open(filename,"r")
file_data = file.readlines() # Put your code here!
print(file_data)


# Read the content of the file, one line at a time, and and initialize 
# the following variables in the order these variables are listed
# mazeWidth, mazeHeight, aNumOfTreasures, aNumOfBombs must be assigned
# an integer value
"""
mazeWidth = # Put your code here!
mazeHeight = # Put your code here!
aNumOfTreasures = # Put your code here!
aNumOfBombs = # Put your code here!
# emptyCell, obstacle, mario must be assigned a string
emptyCell = # Put your code here!
obstacle = # Put your code here!
mario = # Put your code here!
# marioLocationList must contain a list with two elements
# (of type "str") representing the coordinates x and y of Mario's
# location in the maze. For example: ['0', '0']
marioLocationList = # Put your code here!
"""


# obstacleLocationDict must be a dictionary with items formatted as
# follows: {(x,y): -1} if there is a bomb in the cell at location x,y 
# in the maze and {(x,y): 1} if there is a treasure at the location x,y
# in the maze. If the cell is empty at the location x,y in the maze,
# this location is not stored in the dictionary obstacleLocationDict
obstacleLocationDict = {}
# Put your code here!


# bombScoreRatio must be assigned an integer value
"""
bombScoreRatio = # Put your code here!
"""

# For testing and debugging purposes
##print(f"mazeWidth = {mazeWidth}")
##print(f"mazeHeight = {mazeHeight}")
##print(f"aNumOftreasures = {aNumOfTreasures}")
##print(f"aNumOfBombs = {aNumOfBombs}")
##print(f"emptyCell = '{emptyCell}'")
##print(f"obstacle = '{obstacle}'")
##print(f"mario = '{mario}'")     
##print(f"marioLocationList = {marioLocationList}")
##print(f"obstacleLocationDict = {obstacleLocationDict}")
##print(f"bombScoreRatio = {bombScoreRatio}")

# Close the file
# Put your code here!

# Create a maze
theMaze = list()
"""
theMaze = # Put your code here!
"""
# Create the top and bottom boundaries of the maze
# These boundaries are not part of the maze
hBoundary = list()
"""
hBoundary = # Put your code here!
"""
# Place the character (string) "obstacle" in the maze
# This is how we hide the treasures and bombs from the player
# Put your code here!



# Place Mario in the maze
# Put your code here!


         
# Call the appropriate function which computes the location of the
# exit gate and places it in either the top or the bottom boundary
exitGateLocationList = list()
# Put your code here!


# Call the appropriate function to display the maze 
# Put your code here!



print("\n-------")
