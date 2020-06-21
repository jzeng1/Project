# File:    proj1.py
# Author:  Jason Zeng
# Date:    3/10/2017
# Section: 22
# E-mail:  Jzeng1@umbc.edu
# Description:
# This program takes in a range of integers and categorizes them as odd or even
# prime or composite, perfect/abundant/deficient, square, triangular.

MIN_NUM = 1         # minimum number allowed
MAX_NUM = 100000    # maximum number allowed

PERF = "Perfect"    # return values for checkForPerfect function
ABD  = "Abundant"
DEF  = "Deficient"

#This function prints the greeting of the program
def printGreeting():
    print("This program classifies positive integers as Odd/Even, Prime/Composi\
te, Perfect/Abundancet/Deficient, Square, and Triangular.")

#This function prints the table head 
def printTableHead():
    print("Int      Classifications...................................")
    print("-----------------------------------------------------------")

#This function keeps num, odd, prime, perf, square, tri all aligned    
def printTableLine(num, odd, prime, perf, square, tri):
    print('{:6s}   {:4s}   {:9s}   {:9s}   {:5s}   {:10s}'.format(str(num),str(odd),str(prime),str(perf),str(square),str(tri)))
  
#This fuctions checks for vaild input from the user
def getValidInt(minn,maxx):
  userInt = "Enter a number between " + str(minn) + " and " +  str(maxx) + " (inclusive): "
  
  print("Start with which positive integer")
  newStart = int(input(userInt))
  
  while newStart < MIN_NUM or newStart > MAX_NUM:
      print("That number is not allowed. Please try again!")
      newStart2 = int(input(userInt))
      
      while newStart2 < MIN_NUM or newStart2 > MAX_NUM:
        print("That number is not allowed. Please try again!")
        newStart2 = int(input(userInt))
  
      print("End with which positive integer")
      newEnd = int(input("Enter a number between " + str(newStart2) +  " and "+ str(maxx) + " (inclusive): "))
      
      while newEnd < newStart2 or newEnd > MAX_NUM:
        print("That number is not allowed. Please try again!")
        newEnd = int(input("Enter a number between " + str(newStart2) + " and " + str(maxx) + " (inclusive): "))
      
      return newStart2,newEnd
    
  print("End with which positive integer")  
  newEnd = int(input(userInt))
  
  while newEnd > MAX_NUM or newEnd < MIN_NUM:
      print("That number is not allowed. Please try again!")
      newEnd = int(input(userInt))
      
  return newStart,newEnd

#This function checks if the number is a divisor with a remainder of 0    
def isDivisor(origNum, possDiv):
  if origNum % possDiv == 0:
    return True
  else:
    return False

#This function checks for Abundant/Deficient/Perfect
def checkForPerfect(num):
    summ = 0
    x = 1 
    theDivisor = int(num / 2) + 1
    while x < theDivisor:
      x += 1
      if num % x == 0:
        summ += x
        
    if summ > num:
        return ABD
    elif summ == num:
        return PERF
    else:
        return DEF

#This function checks for even and odd numbers
def isOdd(num):
  if num % 2 == 0:
    return "Even"
  else:
    return "Odd"

#This function checks for prime numbers
def isPrime(num):
  count = 2
  x = 0 
  if num == 1:
    return "Neither"
  while count < num:
    if num % count == 0:
      x = 1 
      return "Composite"
    count += 1 
  if x == 0:
      return "Prime"

#This function checks if the numbers is a perfect Square      
def isSquare(num):
    if (num**0.5) % int(num**0.5) == 0:
      return "Square"
    else:
      return ""

#This function chekcs if the number is Triangular
def isTriangular(num):
  count = 0 
  while count < num:
    if count *(count + 1)/2 == num or num == 1:
        return "Triangular"
    count += 1
  return ""

#In this function it calls the many diffrent functions, based on my while loop it take the user# input from getValidInt counting and checking if perf,odd,prime,square,tri all valid and if it# is it will print out the return.      
def main():

    printGreeting()
    numRange = getValidInt(MIN_NUM,MAX_NUM)
    printTableHead()
  
    counter = numRange[0]
    while counter < numRange[1] + 1:
        perf = checkForPerfect(counter)
        odd = isOdd(counter)
        prime = isPrime(counter)
        square = isSquare(counter)
        tri = isTriangular(counter)
        printTableLine(counter, odd, prime, perf, square, tri)
        counter += 1
      
main()
