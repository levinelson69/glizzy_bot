# Glizzy bot program
# Parameters: None
# Returns: None
import random #Importing a random ___
from random import randint #Importing a random number from randint variable

#List of random names with 'names' variable
names = ["Mickey", "Nate", "Jay", "Jess", "Sally", "Annie", "Christopher", "Jake", "Ironone", "Betty"]

def welcome(): #defining welcome function to generate a random name from list and to print the welcome message
    '''
    Purpose: To generate a random name from the list and print out a welcome message
    Parameters: none
    Returns: none
    '''

num = randint(0,9)

name = (names[num])

print("*** Welcome to Mickeys Glizzys ***")
print("*** My name is",name, "***")
print("I will be here to help you to order your hot and ready Sausages")

def main(): #defining the main function for my program
    '''
    Purpose: To generate a random name from the list and print out a welcome message
    Parameters: none
    Returns: none
    '''
    welcome() 

main() #main function used in my program