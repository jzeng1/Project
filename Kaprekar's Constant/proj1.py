# File:    proj1.py
# Author:  Jason Zeng
# Date:    6/3/2017
# Section: 22
# E-mail:  jzeng1@umbc.edu
# Description: Determine the steps require of a give number from the user to get Kaprekar's Constant.

#These are constant to avoid magic numbers this is used in printMenu
ACCESS_CHOICE1 = 1
ACCESS_CHOICE2 = 2
ACCESS_CHOICE3 = 3
ACCESS_CHOICE4 = 4
KAPREKAR_CONSTANT = 6174

########################################################################
# printGreetings() print the greetings of the program                  #
#                                                                      #
# Input:  NONE                                                         #
# Output: NONE it prints the greetings                                 #

def printGreetings():
    print()
    print("Welcome to the Kaprekar's Constant Inquiry Desk!")

########################################################################
# printMenu() print give choices in the menu                           #
#                                                                      #
# Input:  NONE                                                         #
# Output: NONE it prints the Menu                                      #
                                      
def printMenu():
    menuList = [["Count iterations",ACCESS_CHOICE1],
                ["Show work on iterations",ACCESS_CHOICE2],
                ["Exit",ACCESS_CHOICE3]]

    print()
    counter = 0
    while counter < len(menuList):
        print("\t", menuList[counter][1], "-",menuList[counter][0])
        counter += 1

########################################################################
# reversedNum() reversing the number and calcualting the value and the #
#               number of step required to get to 6174 which is        #
#               Kaprekar's Constant.                                   #
#                                                                      #
# Input:  an integer from forDigNum in main()                          #
# Output: return an integer which is the step total                    #

def reversedNum(forDigNum):

    #This is to keep the while loop going till the value is changed
    count = 1
    #Keep track of the number of iterations getting to Kaprekar Constant.
    totalSteps = 0

    #This if statment is if the user input the KAPREKAR_CONSTANT it will
    #Allow it to print the steps
    if int(forDigNum) != KAPREKAR_CONSTANT:
        while count > 0:
            totalSteps += 1

            Listdigits = list(forDigNum)

            #This changes ['6', '9', '9', '3'] to [6, 9, 9, 3] so changing the 
            #string to an integer
            #Which is used to help me order the numbers from greatest to least.
            myResults = [int(x) for x in Listdigits]

            #This list an updated list from myResults in order from greatest to least
            newList = []

            while myResults:
                #arbitrary number in list for results
                minimum = myResults[0]

                #This goes through every element inside the list results
                for index in myResults:
                    if index < minimum:
                        minimum = index

                newList.append(minimum)
                myResults.remove(minimum)

            #This changes [9, 9, 6, 3] to ['9', '9', '6', '3'] so changing 
            #the integer back to a string which is used to help me concatenate
            # the given numbers.
            myResultsInString = [str(x) for x in newList]

            #This concatenate the number as a string in reverse order
            reverseNum = myResultsInString[0] + myResultsInString[1] + myResultsInString[2] + myResultsInString[3]

            #This concatenate the number as a string orignial number
            originalNum = myResultsInString[3] + myResultsInString[2] + myResultsInString[1] + myResultsInString[0]
            
            #Then casting it to an int to be subtracted
            newNum = int(originalNum) - int(reverseNum)

            #This accounts for special number such as 9998 and 4444
            if len(str(newNum)) == ACCESS_CHOICE4:
                
                newNum = int(originalNum) - int(reverseNum)

                #The format of showing the steps
                print()
                print(" STEP",totalSteps)
                print()
                print(" ",originalNum)
                print("-",reverseNum)
                print("  ----")
                print(" ",newNum)

                #Casting newNum to an integer
                forDigNum = str(newNum)
                theResult = int(newNum)
            
                #if the result reaches to the kaperkar constant then it stop the 
                #while loop by changing count to 0 and returning the amount of
                #time it iterated in this while loop
                if theResult == KAPREKAR_CONSTANT:
                    count = 0
                    return totalSteps
            else:
                if newNum == 0:
                    print("Not a Valid number")
                else:
                    #This add a 0 to the empty number 999 to 9990 when inputing
                    #the integer 9998
                    newNum = str(int(originalNum) - int(reverseNum)) + '0'
                    
                    #This is the formating again
                    print()
                    print(" Step",totalSteps)
                    print()
                    print(" ",originalNum)
                    print("-",reverseNum)
                    print(" ----")
                    print(" ",newNum)
                    
                    #Casting newNum to an integer
                    forDigNum = str(newNum)
                    theResult = int(newNum)

                    if theResult == KAPREKAR_CONSTANT:
                        count = 0
                        return totalSteps

    else:
        return totalSteps

########################################################################
# numberOfSteps() Display the number steps taken to get to the number  #
#                 6174 this function is mainly for choice 1 on the menu#
#                                                                      #
# Input:  an integer from forDigNum in main()                          #
# Output: return an integer which is the step total                    #

def numberOfSteps(forDigNum):

    #This is to keep the while loop going till the value is changed
    count = 1

    #Keep track of the number of iterations getting to Kaprekar Constant.
    totalSteps = 0
    zeroSteps = 0

    #if the user input the kaperkar constant then it will return zeroSteps
    #else it counts the iteration 
    if int(forDigNum) == KAPREKAR_CONSTANT:
        return zeroSteps
    else:
        while count > 0:
            totalSteps += 1
            
            Listdigits = list(forDigNum)

            #This changes ['6', '9', '9', '3'] to [6, 9, 9, 3] so changing the string to an integer
            #Which is used to help me order the numbers from greatest to least.
            myResults = [int(x) for x in Listdigits]

            #This list an updated list from myResults in order from greatest to least
            newList = []

            while myResults:

                # arbitrary number in list for results
                minimum = myResults[0]

                #This goes through every element inside the list results
                for index in myResults:
                    if index < minimum:
                        minimum = index

                newList.append(minimum)
                myResults.remove(minimum)

            #This changes [9, 9, 6, 3] to ['9', '9', '6', '3'] so changing the integer back to a
            #string which is used to help me concatenate the given numbers.
            myResultsInString = [str(x) for x in newList]
                
            reverseNum = myResultsInString[0] + myResultsInString[1] + myResultsInString[2] + myResultsInString[3]
            originalNum = myResultsInString[3] + myResultsInString[2] + myResultsInString[1] + myResultsInString[0]

            newNum = int(originalNum) - int(reverseNum)
            
            #This if statment account for the special number 9998 and 4444
            #This code at the bottom is repeated code in the function reverseNum() 
            #without the step format to count the amount of iterations
            if len(str(newNum)) == ACCESS_CHOICE4:
                
                newNum = int(originalNum) - int(reverseNum)

                forDigNum = str(newNum)
                theResult = int(newNum)

                if theResult == KAPREKAR_CONSTANT:
                    count = 0
                    return totalSteps
            else:
                if newNum == 0:
                    return zeroSteps
                else:
                    newNum = str(int(originalNum) - int(reverseNum)) + '0'
                    
                    forDigNum = str(newNum)
                    theResult = int(newNum)
                    
                    if theResult == KAPREKAR_CONSTANT:
                        count = 0
                        return totalSteps

def main():
    #The function is called goes the same for printMenu()
    printGreetings()
    printMenu()

    #Ask for user input from both the menu and the four digit number
    menuChoice = int(input("\nPlease make a menu choice: "))
    forDigNum = input("Please enter a four-digit number: ")

    #This while loop is a sentinal loop where if the user enter 3 it will exit
    #the program other choices from the menu will go to the if statement.
    while menuChoice != ACCESS_CHOICE3:
        if menuChoice == ACCESS_CHOICE1:
            totalSteps = numberOfSteps(forDigNum)
            print()
            print("It took",totalSteps, "steps to reach Kaprekar's constant")

        elif menuChoice == ACCESS_CHOICE2:
            totalSteps = reversedNum(forDigNum)
            print()
            print("It took",totalSteps, "steps to reach Kaprekar's constant")

        printMenu()
        menuChoice = int(input("\nPlease make a menu choice: "))

        if menuChoice != ACCESS_CHOICE3:
            forDigNum = input("Please enter a four-digit number: ")

main()
