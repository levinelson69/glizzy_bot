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











# Menu so that the user can choose either pickup or delivery
print ("Is your order for Pickup or would you like it for Delivery?")
print ("For Pickup please enter 1")
print ("For Delivery please enter 2")
while True:
    try:
        delivery = int(input("Please enter a number "))
        if delivery >= 1 and delivery <= 2:
            if delivery == 1:
                print ("Pickup")
                break

            elif delivery == 2:
                print ("Delivery")
                break
        else:
            print("Number must be 1 or 2")
    except ValueError:
        print("That is not a valid number")
        print("Please enter 1 or 2")











































#Main Function
def main():
    '''
    Purpose: To generate a random name from the list and print out a welcome message
    Parameters: none
    Returns: none
    '''
    welcome()

main()