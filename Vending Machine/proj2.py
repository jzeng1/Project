# File:    proj2.py
# Author:  Jason Zeng
# Date:    4/10/2017
# Section: 22
# E-mail:  jzeng1@umbc.edu
# Description: This program read in the contents of a vending machine from file, setting the
#              inital card balance from user, Display the vending machine, user then make
#              their selction, chekcs the balance of the card, also adds money to the card and
#              updating the txt file.

#This Constant is for the numbers between 0 and 5.
MAX_VAL = 5 
MIN_VAL = 1
#This Constant is for the checkChoices,numBetween,printMenu.
ACCESS_CHOICE1 = 1
ACCESS_CHOICE2 = 2 
ACCESS_CHOICE3 = 3
ACCESS_CHOICE4 = 4
ACCESS_CHOICE5 = 5
#This Constant is for dispVenMachine and getVaildChoiceVen.
SNACK_NAME = 0
SNACK_PRICE = 1
SNACK_QUANTITY = 2
SNACK_LOCATION = 3
#This Constant is for the index for dispVenMachine and getVaildChoiceVen.
LIST_INDEX0 = 0
LIST_INDEX1 = 1
LIST_INDEX2 = 2
LIST_INDEX3 = 3
LIST_INDEX4 = 4
LIST_INDEX5 = 5

##################################################################################
# printGreetings() print out the greetings
# Input:  nothing is being input.
# Output: A print statement.

def printGreetings():
  print("This program simulates a vending machine. You") 
  print("may choose which vending machine you 'load' in") 
  print("and may also specify how much money you have") 
  print("available for purchasing vending machine items.")
  print("")

##################################################################################
# printMenu() print out the greetings
# Input:  nothing is being input.
# Output: A print statement of the menu going through a 2D list

def printMenu():
  menuList = [["Display Vending Machine",ACCESS_CHOICE1],
             ["Make Selection",ACCESS_CHOICE2],
             ["Display Card Balance",ACCESS_CHOICE3],
             ["Add Money to Card",ACCESS_CHOICE4],
             ["Quit",ACCESS_CHOICE5]]
  
  counter = 0
  #the length of the menuList is greater than the counter go through the menuList
  while counter < len(menuList):
    print(menuList[counter][1], "-",menuList[counter][0])
    counter += 1

###############################################################################
# getVaildAmount() this vaildates the amount inputed by the user
# Input:  nothing is being input.
# Output: the amount of moeny they have in the card. (An integer)

def getValidAmount():
  print("Please enter the amount of money you have on your card.")
  userAmount = float(input("Enter a decimal number (greater than or equal to zero): "))
  
  #userAmount is less than 0 it a negative number reprompt the user input
  while userAmount < 0:
    print("The decimal number must be positive.  Please try again!")
    userAmount = float(input("Enter a decimal number (greater than or equal to zero): "))
  return userAmount 

###############################################################################
# checkBalance() this checks the balance in your card
# Input:  integer  
# Output: print statement of the total amount that is in your card.

def checkBalance(amountHad,amountSubtracted):
  
  totalAmount = amountHad - amountSubtracted
  print("You have $", totalAmount, "left on your card.")
  
  return totalAmount
  
##################################################################################
# checkChoices() this vaildates the number inputed by the user
# Input:  nothing is being input.(still thinking of what goes in here)
# Output: the number for the choices

def checkChoices():
  print("")
  userNumber = int(input("Enter a number between 1 and 5 (inclusive): "))
  while userNumber > MAX_VAL or userNumber < MIN_VAL:
      print("That number is not allowed Please try again!")
      userNumber = int(input("Enter a number between 1 and 5 (inclusive): "))
  return userNumber

##################################################################################
# dispVenMachine() this displays what is available in the vending machine
# Input:  A 3D list
# Output: print statement (displays what is available in the vending machine)

def dispVenMachine(theList):

  #theList is a 3D list which are then organized to prompt the correct name, price and location.
  #if the Snack quantity reach a value of zero it will change the index for the name, price and location to what i have assign it to. And this apply to
  #the others.  
  if int(theList[0][LIST_INDEX0][0][SNACK_QUANTITY]) == 0:
    theList[0][LIST_INDEX0][0][SNACK_NAME] = "{EMPTY}"
    theList[0][LIST_INDEX0][0][SNACK_PRICE] = ''
    theList[0][LIST_INDEX0][0][SNACK_LOCATION] = ''
    
  if int(theList[0][LIST_INDEX1][0][SNACK_QUANTITY]) == 0:
    theList[0][LIST_INDEX1][0][SNACK_NAME] = "{EMPTY}"
    theList[0][LIST_INDEX1][0][SNACK_PRICE] = ''
    theList[0][LIST_INDEX1][0][SNACK_LOCATION] = ''
    
  if int(theList[0][LIST_INDEX2][0][SNACK_QUANTITY]) == 0:
    theList[0][LIST_INDEX2][0][SNACK_NAME] = "{EMPTY}"
    theList[0][LIST_INDEX2][0][SNACK_PRICE] = ''
    theList[0][LIST_INDEX2][0][SNACK_LOCATION] = ''
    
  if int(theList[0][LIST_INDEX3][0][SNACK_QUANTITY]) == 0:
    theList[0][LIST_INDEX3][0][SNACK_NAME] = "{EMPTY}"
    theList[0][LIST_INDEX3][0][SNACK_PRICE] = ''
    theList[0][LIST_INDEX3][0][SNACK_LOCATION] = ''
    
  if int(theList[0][LIST_INDEX4][0][SNACK_QUANTITY]) == 0:
    theList[0][LIST_INDEX4][0][SNACK_NAME] = "{EMPTY}"
    theList[0][LIST_INDEX4][0][SNACK_PRICE] = ''
    theList[0][LIST_INDEX4][0][SNACK_LOCATION] = ''
  
  if int(theList[0][LIST_INDEX5][0][SNACK_QUANTITY]) == 0:
    theList[0][LIST_INDEX5][0][SNACK_NAME] = "{EMPTY}"
    theList[0][LIST_INDEX5][0][SNACK_PRICE] = ''
    theList[0][LIST_INDEX5][0][SNACK_LOCATION] = ''

  print('   {:12s}  {:12s}  {:12s}'.format(theList[0][LIST_INDEX0][0][SNACK_NAME],theList[0][LIST_INDEX1][0][SNACK_NAME],theList[0][LIST_INDEX2][0][SNACK_NAME]))
  
  print('   {:12s}  {:12s}  {:12s}'.format(theList[0][LIST_INDEX0][0][SNACK_PRICE],theList[0][LIST_INDEX1][0][SNACK_PRICE],theList[0][LIST_INDEX2][0][SNACK_PRICE]))
  
  print('   {:12s}  {:12s}  {:12s}'.format(theList[0][LIST_INDEX0][0][SNACK_LOCATION],theList[0][LIST_INDEX1][0][SNACK_LOCATION],theList[0][LIST_INDEX2][0][SNACK_LOCATION]))
  
  print("")
  
  print('   {:12s}  {:12s}  {:12s}'.format(theList[0][LIST_INDEX3][0][SNACK_NAME],theList[0][LIST_INDEX4][0][SNACK_NAME],theList[0][LIST_INDEX5][0][SNACK_NAME]))
  
  print('   {:12s}  {:12s}  {:12s}'.format(theList[0][LIST_INDEX3][0][SNACK_PRICE],theList[0][LIST_INDEX4][0][SNACK_PRICE],theList[0][LIST_INDEX5][0][SNACK_PRICE]))
  
  print('   {:12s}  {:12s}  {:12s}'.format(theList[0][LIST_INDEX3][0][SNACK_LOCATION],theList[0][LIST_INDEX4][0][SNACK_LOCATION],theList[0][LIST_INDEX5][0][SNACK_LOCATION]))
  
##################################################################################
# getValidChoiceVen() this vaildates the options of the vending machine inputed by the user
# Input:  nothing is being input
# value when accessing the candi.txt file.
# Output: a print statement that says this option is vaild or not

def getValidChoiceVen(theList,totalNumber):
  #This checks the user input if the user input anything other than the valid inputs then it will say it not a vaild choice and repromt the choices again. 
  inputLocation = input("Please enter one of the choices from the vending machine: ")
  
  while "A1" not in inputLocation and "A2" not in inputLocation and "A3" not in inputLocation and "B1" not in inputLocation and "B2" not in inputLocation and "B3" not in inputLocation:
  
    print("That is not a valid choice, please try again.")
    inputLocation = input("Please enter one of the choices from the vending machine: ")

  #After the user input a vaild input if it is A1 then it will print out the amount you have in your card and the item that you had bought. This appys to
  #code for A2 A3 B1 and so forth.
  if inputLocation == "A1":
    priceOfProduct = float(theList[0][LIST_INDEX0][0][SNACK_PRICE])
    totalNow = totalNumber - priceOfProduct
    
    theQuantity = int(theList[0][LIST_INDEX0][0][SNACK_QUANTITY])

    #This is when theQuantity which is the Snack quantity for the item is subtracted by 1 every time the user input A1. This also appyies to code for A2 A3
    #B1 and so forth. 
    if theQuantity > 0:
      theQuantity -= 1
      theList[0][LIST_INDEX0][0][SNACK_QUANTITY] = theQuantity 
        
    
    print("You now have $", totalNow , "left on your card")
    print("Congrats, you bought a Take10!")
    
  elif inputLocation == "A2":
    priceOfProduct = float(theList[0][LIST_INDEX1][0][SNACK_PRICE])
    totalNow = totalNumber - priceOfProduct
    
    theQuantity = int(theList[0][LIST_INDEX1][0][SNACK_QUANTITY])
    
    if theQuantity > 0:
      theQuantity -= 1
      theList[0][LIST_INDEX1][0][SNACK_QUANTITY] = theQuantity 
      
    print("You now have $", totalNow , "left on your card")
    print("Congrats, you bought a Ereos!")
    
  elif inputLocation == "A3":
    priceOfProduct = float(theList[0][LIST_INDEX2][0][SNACK_PRICE])
    totalNow = totalNumber - priceOfProduct
    
    theQuantity = int(theList[0][LIST_INDEX2][0][SNACK_QUANTITY])
    
    if theQuantity > 0:
      theQuantity -= 1
      theList[0][LIST_INDEX2][0][SNACK_QUANTITY] = theQuantity 
      
    print("You now have $", totalNow , "left on your card")
    print("Congrats, you bought a Twux!")
    
  elif inputLocation == "B1":
    priceOfProduct = float(theList[0][LIST_INDEX3][0][SNACK_PRICE])
    totalNow = totalNumber - priceOfProduct
    
    theQuantity = int(theList[0][LIST_INDEX3][0][SNACK_QUANTITY])
    
    if theQuantity > 0:
      theQuantity -= 1
      theList[0][LIST_INDEX3][0][SNACK_QUANTITY] = theQuantity 
    
    print("You now have $", totalNow , "left on your card")
    print("Congrats, you bought a Fratos!")
    
  elif inputLocation == "B2":
    priceOfProduct = float(theList[0][LIST_INDEX4][0][SNACK_PRICE])
    totalNow = totalNumber - priceOfProduct
    
    theQuantity = int(theList[0][LIST_INDEX4][0][SNACK_QUANTITY])
    
    if theQuantity > 0:
      theQuantity -= 1
      theList[0][LIST_INDEX4][0][SNACK_QUANTITY] = theQuantity 
    
    print("You now have $", totalNow , "left on your card")
    print("Congrats, you bought a Loys!")
    
  elif inputLocation == "B3":
    priceOfProduct = float(theList[0][LIST_INDEX5][0][SNACK_PRICE])
    totalNow = totalNumber - priceOfProduct
    
    theQuantity = int(theList[0][LIST_INDEX5][0][SNACK_QUANTITY])
    
    if theQuantity > 0:
      theQuantity -= 1
      theList[0][LIST_INDEX5][0][SNACK_QUANTITY] = theQuantity 
    
    print("You now have $", totalNow , "left on your card")
    print("Congrats, you bought a N&Ns!")
    
  return [priceOfProduct,theList]
  
##################################################################################
# fileIoAccess() This function opens the txt file that is being inputed from the user
# Input:  None (nothing is being inputed)
# Output: A 3D list after being split.
  
def fileIoAccess():
  
  vendingList = []
  vendingList2 = [[[],[],[],[],[],[]]]
  
  inputFile = input("Please enter file to load machine from: ")
  VendingMachine = open(inputFile)
  
  #This for loop goes through the VendingMachine spliting the strings inside the txt file and assigning the strings to a variable. Which is then appended to
  #a 1D list to a 3D. 
  for line in VendingMachine:
    theProduct, theAmount, inStock, theLocation = line.split()
    theList = theProduct,theAmount,inStock,theLocation
    vendingList.append(list(theList))
    
  for count in range(6):
    vendingList2[0][count].append(vendingList[count])
    
  return [list(vendingList2),inputFile]

##################################################################################
# fileIoAccessEnd() this vaildates the options of the vending machine inputed by the user
# Input: newlist still a 3D list but the values are changed
# value when accessing the candi.txt file.
# Output: saves the edits in to the txt file. Nothing is being output.

def fileIoAccessEnd(newEdits,inputFile):

  #What i did here is a took the value from the updated list from the snack quantity and set it equal to a variable 
  stringOfQuantity1 = str(newEdits[0][LIST_INDEX0][0][SNACK_QUANTITY])
  stringOfQuantity2 = str(newEdits[0][LIST_INDEX1][0][SNACK_QUANTITY])
  stringOfQuantity3 = str(newEdits[0][LIST_INDEX2][0][SNACK_QUANTITY])
  stringOfQuantity4 = str(newEdits[0][LIST_INDEX3][0][SNACK_QUANTITY])
  stringOfQuantity5 = str(newEdits[0][LIST_INDEX4][0][SNACK_QUANTITY])
  stringOfQuantity6 = str(newEdits[0][LIST_INDEX5][0][SNACK_QUANTITY])
    
  #Then set tupleQuantity to a string taking the value from stringOfQuantity creating a tuple
  tupleQuantity1 = "Take10 1.25",stringOfQuantity1,"A1" 
  tupleQuantity2 = "Ereos 1.75",stringOfQuantity2,"A2"
  tupleQuantity3 = "Twux 1.15",stringOfQuantity3,"A3"
  tupleQuantity4 = "Fratos 2.05",stringOfQuantity4,"B1"
  tupleQuantity5 = "Loys 1.99",stringOfQuantity5,"B2"
  tupleQuantity6 = "N&Ns 0.75",stringOfQuantity6,"B3"
    
  #print(tupleQuantity1)
  #print(str(tupleQuantity1) + str(tupleQuantity2) + str(tupleQuantity3) + str(tupleQuantity4) + str(tupleQuantity5) + str(tupleQuantity6))
  
  #I then used Casting to make the tuple a string so that it could be writen in the txt file.
  VendingMachine = open(inputFile, "w")
  VendingMachine.write(str(tupleQuantity1) + str(tupleQuantity2) + str(tupleQuantity3) + str(tupleQuantity4) + str(tupleQuantity5) + str(tupleQuantity6))
  VendingMachine.close()

def main():
  printGreetings()
  
  #When the list is retrun from the fileIoAccess i stored the list in a variable called theList
  theList = fileIoAccess()
  
  #Store the values of all of the added numbers of money
  listAmount = []
  
  #This stores all the values of the amount that the product cost choosen from the user. 
  listAmountBought = []
  
  #This ask the user to input the amount of money they have in their card.
  print("Please enter the amount of money you have on your card.")
  userAmount = float(input("Enter a decimal number (greater than or equal to zero): "))
  
  #userAmount is less than 0 it a negative number reprompt the user input
  while userAmount < 0:
    print("The decimal number must be positive.  Please try again!")
    userAmount = float(input("Enter a decimal number (greater than or equal to zero): "))
    
  listAmount.append(userAmount)
  
  printMenu()
  
  #When the value is return from checkChoices i stored the value to a variable called numBetween
  numBetween = checkChoices()
  
  totalNumber = 0
  #I made it so that if numBetween ever hit 5 from the user it would stop the program.
  while numBetween != ACCESS_CHOICE5:

    #If 1 is inputed from the user it goes here. So forth for the rest of the access_choice. Choice 1 call the function dispvenMachine taking theList and
    #displaying the options available in the vending machine. then it repromts the check choice function till it the user enter 5.
    if numBetween == ACCESS_CHOICE1:
      dispVenMachine(theList[0])
      print("")
      printMenu()
      numBetween = checkChoices()
    
    #For Choice 2 both of the for loop adds the numbers together from listAmount and listAmountBought. Then subtracting both of the value to get the 
    #remainding balance after everything has been bought from the user. This also allow the user to make a selection of what item they want in the vending 
    #machine checking if the value they inputed is valid. 
    elif numBetween == ACCESS_CHOICE2:
      totalNumber = 0
      for index in listAmount:
        totalNumber = totalNumber + index
      
      amountSubtracted = 0 
      for index in listAmountBought:
        amountSubtracted = amountSubtracted + index
      
      totalAmountOfMoney = totalNumber - amountSubtracted
      
      newList = getValidChoiceVen(theList[0],totalAmountOfMoney)
      listAmountBought.append(newList[0])

      #This takes the updated list and stores the value to newEdits which is then put in fileIoAccessEnd 
      newEdits = newList[1]
      fileIoAccessEnd(newEdits,theList[1])
      
      print("")
      printMenu()
      numBetween = checkChoices()
    
    # For choice 3 the two for loop also add the numbers together from listAmount and listAmountBought. Then subtracting both of the value to get the 
    # remainding balance. This Displays the amount of money inside your card.
    elif numBetween == ACCESS_CHOICE3:
      
      totalNumber = 0
      for index in listAmount:
        totalNumber = totalNumber + index
      
      amountSubtracted = 0 
      for index in listAmountBought:
        amountSubtracted = amountSubtracted + index
      
      checkBalance(totalNumber,amountSubtracted)
      print("")
      printMenu()
      numBetween = checkChoices()

    # For choice 4 it goes to getValidAmount to promt the user of how much money they want to input in there card. Then this value is then append into the
    # listAmount which are then added together.
    elif numBetween == ACCESS_CHOICE4:
      addMoney = getValidAmount()
      listAmount.append(addMoney)
      print("")
      printMenu()
      numBetween = checkChoices()

main()
