# Glizzy bot program
import random
from random import randint

#List of random names
names = ["Mickey", "Nate", "Jay", "Jess", "Sally", "Annie", "Christopher", "Jake", "Ironone", "Betty"]

def welcome():
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

def main():
    '''
    Purpose: To generate a random name from the list and print out a welcome message
    Parameters: none
    Returns: none
    '''
    welcome()

main()