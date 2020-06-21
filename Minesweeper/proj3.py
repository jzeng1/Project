# File:    proj2.py
# Author:  Jason Zeng
# Date:    5/1/2017
# Section: 22
# E-mail:  jzeng1@umbc.edu
# Description: This program allows you to play Minesweeper. The object of the game is to flag every mine, using clues about the number of neighboring mines in each field.  To win the game, flag all of the mines (and don't incorrectly flag any non-mine fields). 

EMPTY_FIELD = "."
THE_FLAG = "F"
DETONATED_MINE = "X"
THE_MINE = '*'

########################################################################
# printGreetings() print the greetings of the program                  #
#                                                                      #
# Input:  NONE                                                         #
# Output: NONE it prints the greetings                                 #  

def printGreetings():
  print("\tThis program allows you to play Minesweeper. \n\tThe object of the game is to flag every mine,\n\tusing clues about the number of neighboring \n\tmines in each field. To win the game, flag \n\tall of the mines (and don't incorrectly flag \n\tany non-mine fields). Good luck!\n")
  
########################################################################
# fileIoAccess() opens the txt file and prints out the board           #
#                                                                      #
# Input:  NONE                                                         #
# Output: the board; 2d list                                           #  

def fileIoAccess():
  #This list is for minipulating the values in the board
  listBoard =[]
  inputFile = input("Please enter file to load machine from: ")
  mineBoard = open(inputFile, "r")
  
  #going through mineBoard so that it can be strip then appended to a list
  for eachLine in mineBoard:
    theBoard = eachLine.strip()
    listBoard.append([theBoard])
    
  return listBoard

########################################################################
# hiddenBoard() hides all the elements inside the board                #
#                                                                      #
# Input:  A 2D list from listBoard                                     #
# Output: A 1D updated List                                            #  

def hiddenBoard(listBoard):
  
  #This is the updated List when the values are change to periods to hide the bombs 
  updatedList = []
  #append the top of the row so the "++++++""
  updatedList.append(listBoard[0][0])
  
  #This for loop goes through the index 1 through the end by rows
  for index in range(1,len(listBoard)-1):
    listIndex = list(listBoard[index][0])
    
    #This is if the index reach these values then it will change the values inside to periods
    if index == 1 or index == 2 or index == 3 or index == 4 or index == 5 or index == 6 or index == 7 or index == 8 or index == 9 or index == 10 or index == 11 or index == 12 or index == 13 or index == 14 or index == 15 or index == 16:
      
      #This for loop also goes through the index 1 through the end by rows 
      for index in range(1,len(listBoard)-1):
        listIndex[index] = EMPTY_FIELD
        
    #This join function combines the string inside the list
    joinString  = "".join(listIndex)
    
    #Then it is appended to updatedList
    updatedList.append(joinString)
    
  #append the bottom of the row so the "++++++"  
  updatedList.append(listBoard[0][0])
  
  return updatedList

########################################################################
# bombCounter() counts the amount of bombs in the board                #
#                                                                      #
# Input:  A 2D list from listBoard                                     #
# Output: An integer the sum of the bombs                              #  

def bombCounter(listBoard):
  #This is to allow the string inside the list to be mainipulated. which is why i need another list
  bombCountList = []
  
  #This for loop goes through the index 1 through the end by rows
  for index in range(1,len(listBoard)-1):
    listIndex = list(listBoard[index][0])
    
    #This appends the list into the bombCountList
    bombCountList.append(listIndex)
  
  #This add the total amount of bombs inside the board
  totalBombs = sum(row.count('*') for row in bombCountList)
  print("\tThere are",totalBombs,"mines left to find\n")
  
  return totalBombs

########################################################################
# checkRowsAndColumns() Checks the values for both rows and columns    #
#                                                                      #
# Input:  An integer of the maximun length of the rows and columns     #
# Output: An integer for both rows and columns in a list               #  

def checkRowsAndColumns(maxValue):
  #This is the row portion of the code
  print("Please choose the row:")
  messageRows = "Enter a number between 1 and "+str(maxValue)+" (inclusive): "
  userRows = int(input(messageRows))
  
  #if userRows is greater than the maxValue or userRows is less than 1 then it repromts the user input.
  while userRows > maxValue or userRows < 1:
    print("That number is not allowed Please try again!")
    userRows = int(input(messageRows))
  
  #This is the columns portion of the code
  print("Please choose the columns")
  messageRows = "Enter a number between 1 and "+str(maxValue)+" (inclusive): "
  userColumns = int(input(messageRows))
  
  #if userColumns is greater than the maxValue or userColumns is less than 1 then it repromts the user input.
  while userColumns > maxValue or userColumns < 1:
    print("That number is not allowed Please try again!")
    userColumns = int(input(messageRows))
    
  return userRows,userColumns
  
########################################################################
# checksValidInput() Checks the user input to reveal or flag           #
#                                                                      #
# Input:  NONE                                                         #
# Output: the user input to reveal or to flag so the string f and r    # 
  
def checksValidInput():
  #This ask the user to reveal the spaces or flag it.
  revealOrMark = input("Enter 'r' to reveal the space, or\nenter 'f' to mark the space with a flag: ")
  
  #A while loop if f and r is not inside of revealOrMark then it will repromts the user.
  #while "f" not in revealOrMark and "r" not in revealOrMark:
  while revealOrMark not in ('f','r'):
    print("That's not a valid action.")
    revealOrMark = input("Enter 'r' to reveal the space, or\nenter 'f' to mark the space with a flag: ")
    
  return revealOrMark

########################################################################
# This fxn provided by Dr. Gibson, and may be modified as you see fit. #
########################################################################
# prettyPrintBoard() prints the board with row and column labels,      #
#                    and spaces the board out so that it looks square  #
# Input:             board;   the rectangular 2d gameboard to print    #
# Output:            none;    prints the board in a pretty way         #

def prettyPrintBoard(board):
    # if board is large enough, print a "tens column" line above the rows
    if len(board[0]) - 2 >= 10:
        firstLine = "\n     " + ("  ") * (10 - 1)
        for i in range(10, len(board[0])-1 ):
            firstLine += str(i // 10) + " "
        print(firstLine, end="")

    # create and print top numbered line (and empty line before)
    topLine = "\n     "
    # only go from 1 to len - 1, so we don't number the borders
    for i in range(1, len(board[0])-1 ):
        # only print the last digit (so 15 --> 5)
        topLine += str(i % 10) + " "
    print(topLine)

    # create the border row
    borderRow = "   "
    for col in range(len(board[0])):
        borderRow += board[0][col] + " "

    # print the top border row
    print(borderRow)

    # print all the interior rows
    for row in range(1, len(board) - 1):
        # create the row label on the left
        rowStr = str(row) + " "

        # if it's a one digit number, add an extra space, so they line up
        if row < 10:
            rowStr += " "

        # add the row contents to the row string, and print it out
        for col in range(len(board[row])):
            rowStr += str(board[row][col]) + " "
        print(rowStr)

    # print the bottom border row and an empty line
    print(borderRow)
    print()

def revealBoard(listBoard):
  #This list is updated to reveal the block 
    revealList = []
  
    #This for loop goes through the index through the end by row
    for index in range(len(listBoard)):
    
      #This makes it so that i append the correct values to look like this [0,0,0,0,0]
      revealList1 = [int(0) for index in range(len(listBoard))]
      revealList.append(list(revealList1))
    
      #This minipulats the values it goes the same for the code in the bottom
      revealList[0][index] = 1
    
    for index in range(len(listBoard)):  
      revealList[len(listBoard)-1][index] = 1
    
    #This for loop also goes through the index 1 through the end by rows 
    for index in range(1,len(listBoard)-1):
      revealList[index][0] = 1
      revealList[index][len(listBoard)-1] = 1 
    
    return revealList

################################################################################
# revealingIslandClue() the board that is going to help count the bombs inside #
# the board.                                                                   #
# Input:  A 2D list from bombsClueList,updatedListRevealNormal,An integer both #                      
# valueRows and valueColumns.                                                  #
# Output: A 2D updated List with all the values added up                       # 

def revealingIslandClue(bombsClueList,updatedListRevealNormal,valueRows,valueColumns):
  
  #if bombsClueList[valueRows][valueColumns] >= 1 or valueRows == 0 or valueRows == len(updatedListRevealNormal) or  valueColumns == 0 or len(updatedListRevealNormal):
  #  return bombsClueList
  
  #else: 
    for valueRows in range(len(updatedListRevealNormal)):
      for valueColumns in range(len(updatedListRevealNormal[valueRows])):
        if updatedListRevealNormal[valueRows][valueColumns] == THE_MINE:
          #TOP
          bombsClueList[valueRows-1][valueColumns] += 1
          #BOTTOM
          bombsClueList[valueRows+1][valueColumns] += 1
          #LEFT
          bombsClueList[valueRows][valueColumns-1] += 1
          #RIGHT
          bombsClueList[valueRows][valueColumns+1] += 1
          #TOP CORNER RIGHT
          bombsClueList[valueRows-1][valueColumns+1] += 1
          #TOP LEFT CORNER
          bombsClueList[valueRows-1][valueColumns-1] += 1
          #BOTTOM LEFT
          bombsClueList[valueRows+1][valueColumns-1] += 1
          #BOTTOM RIGHT
          bombsClueList[valueRows+1][valueColumns+1] += 1
        
  #newBombsClueList = [[str(j) for j in i] for i in bombsClueList]
  #return revealingIsland(newBombsClueList, updatedListRevealNormal, valueRows -1 , valueColumns)
 
      #if updatedListRevealNormal[valueRows][valueColumns] == ' ':
        #bombsClueList[valueRows][valueColumns] = ' '
  
    newBombsClueList = [[str(j) for j in i] for i in bombsClueList]
    #print(newBombsClueList)
    return newBombsClueList

######################################################################################
# revealingIsland() the board that is going to help reveal the island using recursion#
#                                                                                    #
# Input:  A 2D list from newbombsClueList,An integer both valueRows and valueColumns #                  
#                                                                                    #
# Output: A 2D updated List with all the values added up                             # 

def revealingIsland(newBombsClueList,valueRows,valueColumns):
  for valueRows in range(len(newBombsClueList)):
      for valueColumns in range(len(newBombsClueList[valueRows])):
        if newBombsClueList[valueRows][valueColumns] == '0':
          newBombsClueList[valueRows][valueColumns] = ' '
  return newBombsClueList
          
  #if newBombsClueList[valueRows][valueColumns] == ' ':
  #  return newBombsClueList
  
  #else: 
    #for valueRows in range(len(newBombsClueList)):
    #  for valueColumns in range(len(newBombsClueList[valueRows])):
    #    if newBombsClueList[valueRows][valueColumns] == '0':
    #      newBombsClueList[valueRows][valueColumns] = ' '
  #  return revealingIsland(newBombsClueList,valueRows -1 , valueColumns)  
  
  #else: 
    #return revealingIsland(newBombsClueList,valueRows -1 , valueColumns)

def main():
  printGreetings()
  listBoard = fileIoAccess()
  updatedList = hiddenBoard(listBoard)
  prettyPrintBoard(updatedList)
  totalMines = bombCounter(listBoard)
  
  #This is used to update 
  updatedListFlag = []
  listCheckForX = []
  updatedListReveal =[]
  updatedListRevealNormal =[]

 #THIS I NEED TO EDIT
  while DETONATED_MINE not in listCheckForX and THE_FLAG not in listCheckForX:
  
    #The Maximum value for the rows and columns.
    theListForBoth = checkRowsAndColumns(len(listBoard) - 2)
    #This is so that i can take the values out for both the rows and columns
    list(theListForBoth)
    #Setting both the values of rows and columns store in the variable.
    valueRows = theListForBoth[0]
    valueColumns = theListForBoth[1]
    #The value f and r to reveal and flag.
    revealOrMark = checksValidInput()
  
    #This function gives clues about where the bomb is located
    bombsClueList = revealBoard(listBoard)
    #print(bombsClueList)
    
  #WHAT IM TRYING TO DO HERE ADD THE BOMBS UP WITH IN THAT LOCATION.
    #This is the updated List when the values are change to periods to hide the bombs 
    updatedList1 = []
    #append the top of the row so the "++++++""
    updatedList1.append(listBoard[0][0])
  
    #This for loop goes through the index 1 through the end by rows
    for index in range(1,len(listBoard)-1):
      listIndex = list(listBoard[index][0])

    #This join function combines the string inside the list
      joinString  = "".join(listIndex)
    
      #Then it is appended to updatedList
      updatedList1.append(joinString)
    
    #append the bottom of the row so the "++++++"  
    updatedList1.append(listBoard[0][0])
    
    #This is used for the function prettyPrintBoard to display the board which is a 1D list
    displayListFlag = []
    displayListReveal = []
    updatedListRevealNormal =[]
    
     #This for loop goes through the index through the end by rows
    for index in range(len(listBoard)):
      listIndexFlag = list(updatedList[index])
      listIndexReveal = list(updatedList1[index])
      
      #This is then appended to updatedListFlag
      updatedListFlag.append(listIndexFlag)
      updatedListReveal.append(listIndexReveal)
      updatedListRevealNormal.append(listIndexReveal)

#This checks to see if updatedListReveal has a bomb from the user rows and columns if there is one present then it changes the element to 'X' which is the DETONATED_MINE
    
    #if the updatedListFlag is a '.' and revealOrMark is equal to f then it will append the flag into the list.  
    if updatedListFlag[valueRows][valueColumns] == EMPTY_FIELD and revealOrMark == 'f':
      
      #From the user input of rows and columns this changes the elements inside updatedListFlag which is a 2D list changing its values to THE_FLAG.
      updatedListFlag[valueRows][valueColumns] = THE_FLAG
      updatedListReveal[valueRows][valueColumns] = THE_FLAG
    
      #This for loop goes through the index through the end by row
      for index in range(len(listBoard)):
      
        #This join function combines the string inside the list
        joinList = "".join(updatedListFlag[index])
        joinList1 = "".join(updatedListReveal[index])
        
        #Then its appended to displayListFlag
        displayListFlag.append(joinList)
        displayListReveal.append(joinList1)
        
      #Displays the updated board    
      prettyPrintBoard(displayListFlag)
      
      #Subtract the total in totalMines when the user enter f.
      totalMines -= 1
      print("\tThere are",totalMines,"mines left to find\n")
      
    #if the updatedListFlag is a 'F' and revealOrMark is equal to f then it will remove the flag from the list.
    elif updatedListFlag[valueRows][valueColumns] == THE_FLAG and revealOrMark == 'f':
      #From the user input of rows and columns this changes the elements inside updatedListFlag which is a 
      #2D list changing its values to THE_FLAG.
      updatedListFlag[valueRows][valueColumns] = EMPTY_FIELD
      
      #This is then appended to updatedListFlag
      
      if updatedList1[valueRows][valueColumns] == THE_MINE:
        updatedListReveal[valueRows][valueColumns] = THE_MINE
        
      elif updatedList1[valueRows][valueColumns] == ' ':
        updatedListReveal[valueRows][valueColumns] = ' '
        
      #This for loop goes through the index through the end by rows
      for index in range(len(listBoard)):
      
        #This join function combines the string inside the list
        joinList = "".join(updatedListFlag[index])
        joinList1 = "".join(updatedListReveal[index])
      
        #Then its appended to displayListFlag
        displayListFlag.append(joinList)
        displayListReveal.append(joinList1)
        
      prettyPrintBoard(displayListFlag)
      totalMines += 1
      print("\tFlag removed from",valueRows,",",valueColumns)
      print("\tThere are",totalMines,"mines left to find\n")
#STORE THE UPDATED VALUE SO IT CAN BE TURN INTO A STRING TO CHECK IF THERE IS '*' INSIDE THE updatedListReveal
    if updatedListFlag[valueRows][valueColumns] == THE_FLAG and revealOrMark == 'f':
      testList = []
      for index in range(1,len(listBoard)-1):
        #print(str(displayListReveal[index]))
        testList.append(str(displayListReveal[index]))
    if totalMines == 0:
      if '*' not in str(testList):
        listCheckForX.append(THE_FLAG)
        print("You won! Congratulations, and good game!")
    
    #if the updatedListFlag is a 'F' and revealOrMark is equal to r then it will prompt the user to unflag the position they flaged.
    if updatedListFlag[valueRows][valueColumns] == THE_FLAG and revealOrMark == 'r':
      for index in range(len(listBoard)):
      
        #This join function combines the string inside the list
        joinList = "".join(updatedListFlag[index])
      
        #Then its appended to displayListFlag
        displayListFlag.append(joinList)
      prettyPrintBoard(displayListFlag)
      print("\tField",valueRows,",",valueColumns,"must be unflagged before it can be revealed")
      print("\tThere are",totalMines,"mines left to find\n")
      
    #if the updatedListFlag can not equal to 'F' and revealOrMark is equal to r then it will reveal the item under that block.
    elif updatedListFlag[valueRows][valueColumns] != THE_FLAG and revealOrMark == 'r':  
      #This for loop goes through the index through the end by rows
      for index in range(len(listBoard)):
        listIndexFlag = list(updatedList[index])
      
        #This is then appended to updatedListFlag
        updatedListFlag.append(listIndexFlag)
      
      #From the user input of rows and columns this changes the elements inside updatedListFlag which is a 
      #if updatedListReveal is the '*' then the value changes to 'x'
      if updatedListRevealNormal[valueRows][valueColumns] == THE_MINE:
         updatedListRevealNormal[valueRows][valueColumns] = DETONATED_MINE
         updatedListFlag[valueRows][valueColumns] = updatedListRevealNormal[valueRows][valueColumns]
      else:
        newBombsClueList = revealingIslandClue(bombsClueList,updatedListRevealNormal,valueRows,valueColumns)
        revealingIsland(newBombsClueList,valueRows,valueColumns)

        updatedListFlag[valueRows][valueColumns] = newBombsClueList[valueRows][valueColumns]
      
      #This for loop goes through the index through the end by rows
      for index in range(len(listBoard)):
      
        #This join function combines the string inside the list
        joinList = "".join(updatedListFlag[index])
      
        #Then its appended to displayListFlag
        displayListFlag.append(joinList)
      
      #THIS IS THE GAME OVER PORITON OF THE CODE
      if updatedListFlag[valueRows][valueColumns] == DETONATED_MINE:
        listCheckForX.append(DETONATED_MINE)
        prettyPrintBoard(displayListFlag)
        print("You detonated a mine!  Game Over!")
      
      else:
        prettyPrintBoard(displayListFlag)
        print("\tThere are",totalMines,"mines left to find\n")
  
main()
