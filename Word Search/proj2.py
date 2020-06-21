# File:    proj2.py
# Author:  Jason Zeng
# Date:    6/10/2017
# Section: 22
# E-mail:  jzeng1@umbc.edu
# Description: This Program will find the word inside the txt file print out each word that was found or not. 
#              If the word is found the coordinate for the word is shown, also the direction.

#Constant that i am gonna use in the reccusive portion of the program also
#the sense of direction for the function updatedCoordinates()

UP_DIRECTION = 'up'
DOWN_DIRECTION = 'down'
LEFT_DIRECTION = 'backwards left'
RIGHT_DIRECTION = 'right'
UPPER_RIGHTCORNER = 'diagonally up and right'
UPPER_LEFTCORNER = 'diagonally up and left'
BOTTOM_LEFTCORNER = 'diagonally down and left'
BOTTOM_RIGHTCONER = 'diagonally down and right'
NOT_FOUND = 'None'

########################################################################
# printGreetings() print the greetings of the program                  #
#                                                                      #
# Input:  NONE                                                         #
# Output: NONE it prints the greetings                                 #

def printGreetings():
    print("Welcome to the Word Search")
    print("For this, you will import two files: ")
    print()
    print("\t1. The word search grid")
    print("\t2. The word list")
    print()

########################################################################
# fileIoAccessWord() opens the txt file and prints out the board       #
#                                                                      #
# Input:  NONE                                                         #
# Output: the board; 1d list                                           #

def fileIoAccessWord():
    #This list contain all of the words
    listWords = []

    inputWord = input("What word list file would you like to import?: ")
    wordToFind = open(inputWord, "r")

    #going through wordToFind so that it can be split then appended to a list
    for eachLine in wordToFind:
        theWord = eachLine.strip()
        listWords.append(theWord)

    #This closes the file
    wordToFind.close()
    print()

    return listWords

########################################################################
#findFirstLetter() finds the first letter of the word in the board of  #
#                  of the given word                                   #
#                                                                      #
# Input:  2D,1D list theBoard,theWord                                  #
# Output: 2D List of the coordinate                                    #

def findFirstLetter(theBoard,theWord):
    
    #This make it a 2d list of the coordinates
    startList =[]
    
    for row in range(len(theBoard)):
        for col in range(len(theBoard)):
            
            if theBoard[row][col] == theWord[0]:
                coordinatePoints = (row,col)
                startList.append(list(coordinatePoints))

    return startList

#####################################################################################
#checkTheDirection() This is a key that allow me to keep track of what direction    #
#                    the word is found printing out if the puzzle is going up down, #
#                    left,right etc.                                                #
#                                                                                   #
# Input:  string of the direction like U,D,L,R,UR etc.                              #
# Output: return a string from the constant that i assigned it to.                  #

def checkTheDirection(directionOfFound):

    #if directionOfFound is U then it return up as a string it goes the same for the code below.
    if directionOfFound == 'U':
        return UP_DIRECTION

    elif directionOfFound == 'D':
        return DOWN_DIRECTION

    elif directionOfFound == 'L':
        return LEFT_DIRECTION

    elif directionOfFound == 'R':
        return RIGHT_DIRECTION

    elif directionOfFound == 'UR':
        return UPPER_RIGHTCORNER

    elif directionOfFound == 'UL':
        return UPPER_LEFTCORNER

    elif directionOfFound == 'BL':
        return BOTTOM_LEFTCORNER

    elif directionOfFound == 'BR':
        return BOTTOM_RIGHTCONER
    else:
        return NOT_FOUND


########################################################################################################
#checkForWord() This uses recursion, checking the letter surrounding                                   #
#               The first letter of the word given from the coordinate                                 #
#                                                                                                      #
# Input:  2D list theBoard, row(int), column(int), numRows(int), numCols(integer), direction(string)   #
# Output: A boolen wordFound, a string of the currentDirection                                         #

def checkForWord(board, row, column, word, numRows, numCols, direction):
    
    currentDirection = 'None'
    wordFound = False

    #This is the base case where the program is gonna stop i have it return a boolen.
    if (row > (numRows - 1) or column > (numCols - 1) or row< 0 or column < 0):
        return False

    #This goes through every single character in the puzzle and if it equal the first letter of the word
    #it has found the location of where it should check the 8 direction.
    elif (board[row][column] == word[0]):

        #if the length of the word is 1 then it has found the word and return a boolen which it true
        if(len(word) == 1):
            return (True, currentDirection)

        #The direction is going up
        #this pretty much applies for the code down below of the 8 diffrent direction duplicate code.
        if (not wordFound and row - 1 >= 0 and column >= 0 and (direction == 'START' or direction == 'U')):

            #This is the recursive case for the direction going up the word[1:] slices the word
            #when the letter of the word is found. the row - 1 indicate the direction which is up.
            wordFound, currentDirection = checkForWord(board, row - 1, column , word[1:], numRows, numCols, 'U')

            #This is the key indicating which direction it goes, but for this case it up.
            currentDirection = 'U'

        #The direction going down
        if (not wordFound and row + 1 <= (numRows - 1) and column >= 0 and (direction == 'START' or direction == 'D')):

            wordFound, currentDirection = checkForWord(board, row + 1, column , word[1:], numRows, numCols, 'D')

            currentDirection = 'D'

        #The direction going Left
        if (not wordFound and row >= 0 and column - 1 >= 0 and (direction == 'START' or direction == 'L')):

            wordFound, currentDirection = checkForWord(board, row , column - 1, word[1:], numRows, numCols, 'L')

            currentDirection = 'L'

        #The direction going right
        if (not wordFound and row >= 0 and column + 1 <= (numCols - 1)and (direction == 'START' or direction == 'R')):

            wordFound, currentDirection = checkForWord(board, row, column + 1, word[1:], numRows, numCols, 'R')

            currentDirection = 'R'

        #The direction going diagonally up right
        if (not wordFound and (row - 1) >= 0 and (column + 1) <= (numCols - 1) and (direction == 'START' or direction == 'UR')):

            wordFound, currentDirection = checkForWord(board, row - 1, column + 1, word[1:], numRows, numCols, 'UR')

            currentDirection = 'UR'

        #The direction going diagonally up left
        if (not wordFound and row - 1 >= 0 and column - 1 >= 0 and (direction == 'START' or direction == 'UL')):

            wordFound, currentDirection = checkForWord(board, row - 1, column - 1, word[1:], numRows, numCols, 'UL')

            currentDirection = 'UL'

        #The direction going diagonally down left
        if (not wordFound and row + 1 <= (numRows - 1) and column - 1 >= 0 and (direction == 'START' or direction == 'BL')):

            wordFound, currentDirection = checkForWord(board, row + 1, column - 1, word[1:], numRows, numCols, 'BL')

            currentDirection = 'BL'

        #The direction going diagonally down right
        if (not wordFound and row + 1 <= (numRows - 1) and column + 1 <= (numCols - 1)and (direction == 'START' or direction == 'BR')):
            
            wordFound, currentDirection = checkForWord(board, row + 1, column + 1, word[1:], numRows, numCols, 'BR')
            
            currentDirection = 'BR'

    return (wordFound, currentDirection)



##############################################################################
#updatedCoordinates() This function print the word,coordinate and            #
#                     the direction it goes. checking if the word is found   #
#                     or not.                                                #
# Input:  2D list theBoard, word string, coord list of coordinate            #
# Output: NONE gonna print out the word coordinate and the direction it goes #

def updatedCoordinates(listBoard,myWord,numRows,numColumns):

    #This initializes the indexRows and indexColumns
    indexRows = 0
    indexColumns = 0

    startingDirection = 'Starting'

    #This variable is so that I can make sure that wordFound is false
    #when its running till the word is found.
    wordFound = False

    for indexRows in range (0,numRows):
        for  indexColumns in range (0, numColumns):

            #The function checkForWord is called value are return like this
            #(wordFound,startingDirection) are (false,U)
            wordFound,startingDirection = checkForWord(listBoard, indexRows, indexColumns, myWord, numRows, numColumns ,'START')

            if wordFound == True:
                print("The word " + myWord + " starts in " + str(indexRows) + ", " + str(indexColumns) + " and goes " + checkTheDirection(startingDirection))
                return

    if wordFound == False:
        print("The word "+ str(myWord) + " does not appear in the puzzle.")

def main():

    printGreetings()

    #This list contains value inside the board creating a 2d list
    listBoard = []

    #This variable is to put numRows and numColumns before the assignment so i just made it equal to zero.
    numRows =  0
    numColumns = 0

    #This open the p.txt file
    inputSearch = input("What word search grid file would you like to import?: ")
    wordBoard = open(inputSearch, "r")

    #going through wordBoard so that it can be split then appended to a list
    for eachLine in wordBoard:
        theBoard = eachLine.split()
        listBoard.append(list(theBoard))

        #both of these check the length and width of the puzzle later gonna be used for the bounds.
        numColumns = len(theBoard)
        numRows = len(theBoard)

    #This closes the file for p.txt
    wordBoard.close()

    #Function call from fileIoAccessWord to get the 1D list of words.
    theWord = fileIoAccessWord()

    #Iterating through theWord
    for myWord in theWord:

        #The function is called in updatedCoordinates
        updatedCoordinates(listBoard,myWord,numRows,numColumns)


main()
