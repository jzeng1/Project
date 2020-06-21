# File:    proj3.py
# Author:  Jason Zeng
# Date:    6/18/2017
# Section: 22
# E-mail:  jzeng1@umbc.edu
# Description: This Program will indicate if the final food cordinated with the
#              color levers with a set amount of rules for each. if the food is
#              edible or containmated with what color.

VALUE_TWO = 2

########################################################################
# fileIoAccessColor() opens the txt file and prints out the board      #
#                                                                      #
# Input:  NONE                                                         #
# Output: the board; 1d list                                           #

def fileIoAccessColor():

  #This list contain all of the words
  listOfColors = []

  inputColor = input("Please enter a file for input: ")
  colorToFind = open(inputColor,"r")

  #going through colorToFind so that it can be split then appended to a list
  for eachLine in colorToFind:
      theColor = eachLine.strip()
      listOfColors.append(theColor)

  #This closes the file
  colorToFind.close()

  return listOfColors

#########################################################################
# firstLever() This indicates which path it going first so if the first #
#              value is white then it remove white from the list and is #
#              called to another function called whiteLever.            #
# Input:  1d list of the colors, string the color                       #
# Output: NONE                                                          #

def firstLever(listOfColor,otherColor):

   #If the otherColor is white which is the first element in the listOfColor then it removes
   #white an example output would be [white,green,black,white] to [green,black,white]
   if otherColor == 'white':
       listOfColor.remove('white')

      #This call whiteLever and send the next color in the list with the updated list.
      #an example output would be (white ['white', 'green', 'black', 'white', 'green', 'yellow', 'red'])
      #This pretty much work the same as the other color levers function i have down below just repeated code
      #with the corresponding color Lever function.
       whiteLever(listOfColor[0],listOfColor)

   elif otherColor =='black':
       listOfColor.remove('black')
       blackLever(listOfColor[0],listOfColor)
   
   #This is here if other color are presented other than black or white and will go straight to yellowLever to 
   #print the color tha has broken the rule.
   else:
       yellowLever(listOfColor)

########################################################################
# whiteLever() This indicates if the path is going either green or     #
#              white. If the next color is white then it goes to this  #
#              function.                                               #
#                                                                      #
# Input:  string the updated color, 1d list of the color that updated  #
# Output: NONE                                                         #

def whiteLever(otherColor,listOfColor):

    if otherColor == 'green':
        listOfColor.remove('green')
        greenLever(listOfColor[0],listOfColor)

    elif otherColor =='white':
        listOfColor.remove('white')
        whiteLever(listOfColor[0],listOfColor)

    else:
        yellowLever(listOfColor)

#########################################################################
# blackLever() This indicates if the path is going either white or      #
#              red. If the next color is black then it goes to this     #
#              function.                                                #
#                                                                       #
# Input:  string the updated color, 1d list of the color that updated   #
# Output: NONE                                                          #

def blackLever(otherColor,listOfColor):

    if otherColor == 'white':
        listOfColor.remove('white')
        whiteLever(listOfColor[0],listOfColor)

    elif otherColor == 'red':
        listOfColor.remove('red')
        redLever(listOfColor[0],listOfColor)

    else:
        yellowLever(listOfColor)

########################################################################
# redLever()This indicates if the path is going red. If the next color #
#           is red then it goes to this function.                      #
#                                                                      #
# Input:  string the updated color, 1d list of the color that updated  #
# Output: NONE                                                         #

def redLever(otherColor,listOfColor):
    
    #For the red Lever is a little diffrent i have it so that i keep looping red till it 
    #changes the color inside the list
    if otherColor == 'red':
        listOfColor.remove('red')
        redLever(listOfColor[0],listOfColor)

    else:
        yellowLever(listOfColor)

#########################################################################
# greenLever() This indicates if the path is going either black or      #
#              yellow. If the next color is green then it goes to this  #
#              function.                                                #
#                                                                       #
# Input: string the updated color, 1d list of the color that updated    #
# Output: NONE                                                          #

def greenLever(otherColor,listOfColor):
    
    if otherColor == 'black':
        listOfColor.remove('black')
        blackLever(listOfColor[0],listOfColor)
    
    elif otherColor == 'yellow':
        yellowLever(listOfColor)

    else:
        yellowLever(listOfColor)

#########################################################################
# yellowLever() This checks if the food is edible or not if its edible  #
#               it would check if the last two levers are yellow if not #
#               then it not edible                                      #
#                                                                       #
# Input: string the updated color, 1d list of the color that updated    #
# Output: print if the food is edible or not.                           #

def yellowLever(theColor):

    #if the length of the final updated list is 1 then it goes here checking the color.
    if len(theColor) == 1:
        if theColor[len(theColor) - 1] == 'yellow':
            print('You pull a', theColor[len(theColor) - 1],'lever, and the food is inedible.')
        else:
            print('You pull a', theColor[len(theColor) - 1],'lever, and the food is inedible.')

    #if the end result in 2 element inside the updated list it goes here.
    if len(theColor) == VALUE_TWO:

      #This is only if the last two levers are yellow it will print out the final food is edible.
      if theColor[len(theColor) - VALUE_TWO] == 'yellow' and theColor[len(theColor) - 1] == 'yellow':
        print('The final food is edible.')
                
      #This indicates if yellow is not inside either the second to last lever or the first to last
      #lever then it will print the color that is containmating the food making it inedible.
      elif 'yellow' not in theColor[len(theColor) - VALUE_TWO]:
        print('You pull a', theColor[len(theColor) - VALUE_TWO],'lever, and the food is inedible.')

      elif 'yellow' not in theColor[len(theColor) - 1]:
        print('You pull a', theColor[len(theColor) - 1],'lever, and the food is inedible.')
    
    #I put this if statement if the lenght of theColor is greater than 2 
    #so if the len of the list is more than 2 or 1 then the rule for 
    #of the color is broken telling you the color that is causing it.
    if len(theColor) > VALUE_TWO:
      print("You pull a", theColor[0], 'lever, and the food is inediable.')

def main():

    theColor = fileIoAccessColor()

    #This is to intialized the value otherColor with the first element inside the list
    otherColor = theColor[0]
    firstLever(theColor,otherColor)

main()
