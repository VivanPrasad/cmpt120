# MyMarioGame_A4.py
# 
# Description: Set up the Mario game by reading data from the input data file
#              and using this data to initialize variables, then create and
#              display the maze in which Mario is to move.
#
# Author: Anne Lavergne, Mahir Vivan Prasad
#
# Date Created: Sunday Nov. 5 2023
# Date Updated: Sunday Nov. 5 2023

# DISCLAIMER: I type hinted parameters of the premade functions
# Type hinting makes it much more easier to find errors!

# -------------------------------------------------------------------

def createMaze(aMaze : list[list[str]], 
        aWidth:int, aHeight:int, aCell:str) -> list[list[str]]:
    ''' Create and return "aMaze" of "aWidth" by "aHeight".
        Each cell of the maze is a string set to "aCell".      
    '''
    aMaze = [ [ (aCell) for i in range(aWidth) ] for j in range(aHeight) ]
    
    return aMaze

# -------------------------------------------------------------------

# Print Maze - This function is to used for testing and debugging purposes only!
def printMaze(aMaze:list[list[str]], aHeight:int) -> None:
    ''' Print "aMaze" of "aHeight" - for testing and debugging purposes.
    ''' 
    for row in range(aHeight):
        print(aMaze[row])  
    return
		
# -------------------------------------------------------------------

def createBoundaryList(aWidth:int, bH = "---") -> list[list[str]]:
    ''' Create and return a list that contains 2 lists: the first list
        is the top boundary of the maze and contains a string set to "bH".
        The second list is the bottom boundary of the maze and it also
        contains a string set to "bH".

        Other parameter:
         "aWidth" is the width of the maze.
    '''
    return list([[(bH) for number in range(aWidth)],
                 [(bH) for number in range(aWidth)]])                

# -------------------------- Maze Display ---------------------------

def displayMaze(aMaze:list[list[str]],
        aWidth:int,aHeight:int,hBoundary:list[list[str]], bS:str = "|"):
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

# ---------------------- Placement Functions ------------------------

def placeExitGate(aWidth:int, aHeight:int, rowMario:int, columnMario:int, 
        hBoundary:list[list[str]], exitGate:str = " = "):
    global exitGateLocationList
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

    return exitGateLocationList  

def placeObstacles(obstacleLocations):
    ''' Place obstacles into the maze
    '''
    for coordinate in obstacleLocations.keys():
        columnObstacle, rowObstacle = coordinate
        theMaze[columnObstacle][rowObstacle] = obstacle

def placeMario(posMario):
    ''' Place the Mario in the maze at his location.
	Mario's location at coordinates ("columnMario","rowMario").
    '''
    columnMario,rowMario = posMario
    theMaze[columnMario][rowMario] = mario

# ------------------------- Get File Data ---------------------------

def get_file_data(filename) -> list[str]:
    '''Opens and reads the file. 
    Returns a list of strings.
    '''

    # Open file for reading
    file = open(filename,"r")
    # Gets the original text from the file
    file_raw_data = file.readlines()
    data = []
    for element in file_raw_data:
        if not element.strip().isnumeric(): # If contains symbols
            # Just remove the \n, NOT the spaces
            data.append(element.removesuffix("\n"))
        else:
            # If contains numbers, strip \n
            data.append(element.strip())
    # Close file
    file.close()
    return data

# ------------------------ Position Functions -----------------------

def get_position(coordinate : str) -> list[int]:
    '''Converts 'y x' to ['y','x'].
    Returns a list with 2 integers for column, row
    '''
    y,x = [int(a) for a in coordinate.split(" ")]
    return [int(y),int(x)]

def get_obstacle_locations():
    '''Adds all locations of treasures and bombs to obstacleLocationDict
    '''
    global file_data, obstacleLocationDict
    for line in range(8,53):
        obstacle_pos : list[int] = get_position(file_data[line])
        if line < 23: #If treasure
            obstacleLocationDict[tuple(obstacle_pos)] = 1
        else: #If bomb
            obstacleLocationDict[tuple(obstacle_pos)] = -1
    return

# --------------- Initialize Variables with No Data -----------------

mazeWidth : int = 0
mazeHeight : int = 0
aNumOfTreasures : int = 0
aNumOfBombs : int = 0

emptyCell : str = ""
obstacle : str = ""
mario : str = ""

marioLocationList : list[int] = []
obstacleLocationDict : dict = {}

marioScore : int = 0 #For assignment 5
bombScoreRatio : int = 0

exitGateLocationList : list[int] = list()

theMaze: list[list[str]] = list()
hBoundary: list[list[str]] = list()

# ------------------------- Maze Setup ------------------------------

def set_game_data(file_data : list[str]) -> None:
    '''Set all the variables using the 
    elements in the file data parameter.
    '''

    # Get the global variables to set in the function
    global mazeWidth, mazeHeight, aNumOfTreasures, aNumOfBombs
    global emptyCell, obstacle, mario
    global marioLocationList, bombScoreRatio, marioScore

    mazeWidth = int(file_data[0])
    mazeHeight = int(file_data[1])
    aNumOfTreasures = int(file_data[2])
    aNumOfBombs = int(file_data[3])

    emptyCell = file_data[4]
    obstacle = file_data[5]
    mario = file_data[6]

    marioLocationList = get_position(file_data[7])

    bombScoreRatio = int(file_data[53])
    marioScore = aNumOfBombs // bombScoreRatio #For assignment 5

    return

def setup_maze() -> None:
    '''Sets up the maze with 
    placements of all objects and mario.
    '''

    # Get the global variables to set in the function
    global marioLocationList, bombScoreRatio, exitGateLocationList
    global theMaze, hBoundary

    # Create a maze and boundary
    theMaze = createMaze(theMaze,mazeWidth,mazeHeight,emptyCell)
    hBoundary = createBoundaryList(mazeWidth)

    exitGateLocationList = placeExitGate(mazeWidth, mazeHeight, 
        marioLocationList[0],marioLocationList[1],hBoundary)
   
    #Set all obstacle locations and add them to obstacleLocationDict
    get_obstacle_locations()

    # Place the character (string) "obstacle" in the maze
    placeObstacles(obstacleLocationDict)

    # Place Mario in the maze (draws on top of obstacles)
    placeMario(marioLocationList)
    
    return
# -------------------------------------------------------------------
#                        MAIN PART OF PROGRAM                       
# -------------------------------------------------------------------


# Welcome the user and identify the game
print("""Welcome to my Mario game.\n""")

# Ask user for filename
filename = input("Please, enter a filename: ")
# Initialize file_data
file_data = get_file_data(filename)

# Set all the variables and their respective data
set_game_data(file_data)
# Sets up the maze size, exit gate, obstacles and mario
setup_maze()

# Call the appropriate function to display the maze 
displayMaze(theMaze,mazeWidth,mazeHeight,hBoundary)

'''
# -------------------------------------------------------------------
#                       Assignment 5 (Part 2)
# -------------------------------------------------------------------

# I found an old PDF of the Mario Game assignment.
# I thought it would be fun to tackle going "ahead"!
# Based on https://www.sfu.ca/~alavergn/120/Assignments/Assn_2.pdf

# Print out a one-time instruction tutorial 
# instead of repeatedly asking user


# -------------------------------------------------------------------

def moveMario(posMario:list[int],vector:list[int]):
    global marioLocationList, obstacleLocationDict, theMaze, marioScore
    y,x,dy,dx = posMario + vector
    new_position = [y+dy,x+dx]
    if marioLocationList == exitGateLocationList:
        if new_position == [-1,0] or new_position == [mazeHeight,mazeWidth-1]:
            marioLocationList = new_position
    if (y+dy) < mazeHeight and (x+dx) < mazeWidth and \
         (x+dx) >= 0 and (y+dy) >= 0:
        marioLocationList = new_position
        theMaze[y][x] = emptyCell
        if theMaze[y+dy][x+dx] == obstacle:
            marioScore += obstacleLocationDict[tuple(new_position)]
        theMaze[y+dy][x+dx] = mario
    

    return
# -------------------------------------------------------------------

#Prints instructions to show off my ASCII art skills :)
print(f"""
║.............How to Play.............║
┌─────────────────────┬───────────────┐
│ Objective           │ Controls      │
├─────────────────────┼───────────────┤
│ Escape the maze!    │ 'r' -> Right  │
│ Risk collecting     │ 'l' -> Left   │
│ treasure.. or bombs!│ 'u' -> Up     │
│ Reach 0 points...   │ 'd' -> Down   │
│ and it's game over! │ ('x' to Quit) │
└─────────────────────┴───────────────┘      
║........................Tiles.........................║
┌─────────────────────┬────────────────────────────────┐
│ Empty ({emptyCell})         │ Obstacle ({obstacle})                 │
├─────────────────────┼────────────────────────────────┤ 
│ Can move to. Just a │ Can move to. Contains either   │  
│ normal ol' tile.    │ treasure (+1pt) or bomb (-1pt) │
└─────────────────────┴────────────────────────────────┘       
┌─────────────────────┬────────────────────────────────┐
│ Mario ({mario})         │ Exit Gate (=)                  │ 
├─────────────────────┼────────────────────────────────┤
│ It's you!           │ Reach it to escape the maze!   │
└─────────────────────┴────────────────────────────────┘
""")

#Constant movement vectors to apply to mario's position
moveVectors : dict = {"r":[0,1],"l":[0,-1],"u":[-1,0],"d":[1,0]}

userInput = ""
while marioScore > 0:
    #Displays updated maze
    displayMaze(theMaze,mazeWidth,mazeHeight,hBoundary)

    #Prints Mario's score
    print(f"\nMario's score -> {marioScore}.\n")
    
    
    #Handles user input to move or exit
    userInput = input("What will you do?: ").lower().strip()
    if userInput == "x":
        break
    
    while not userInput in moveVectors.keys():
        userInput = input("Invalid command. Try again: ").lower().strip()
    
    #Handles movement of mario, updated treasure and collision
    moveMario(marioLocationList, moveVectors[userInput])

    #Reaches gate
    if marioLocationList == [-1,0] or marioLocationList == [mazeHeight,mazeWidth-1]:
        break

#Check condition after game has ended (exit, win or lose)
if userInput == "x":
    pass
elif marioScore > 0:
    print(f"Mario has reached the exit gate\
with a score of {marioScore}! You win!")
else:
    print("Mario's score is now down to 0! You have lost!")

'''

print("\n-------")
