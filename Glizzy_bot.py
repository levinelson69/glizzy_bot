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

#Customer details dictonary 
customer_details = {}
# Validates inputs to check if they are blank
def not_blank(question):
    valid = False
    while not valid:
        response = input(question)
        if response != "":
            return response
        else:
            print("This cannot be blank")



# Menu so that the user can choose either pickup or delivery
def order_type():
    del_pick = ""
    print ("Is your order for pickup or delivery?")
    print ("For pickup please enter 1")
    print ("For delivery please enter 2")
    while True:
        try:
            delivery = int(input("Please enter a number "))
            if delivery >= 1 and delivery <= 2:
                if delivery == 1:
                    print ("Pickup")
                    del_pick = "pickup"
                    pickup_info()
                    break
                elif delivery == 2:
                    print ("Delivery")
                    delivery_info()
                    del_pick = "delivery"
                    break
            else:
                print("Number must be 1 or 2")
        except ValueError:
            print("That is not a valid number")
            print("Please enter 1 or 2")
    return del_pick

#Pickup Information - Name and Phone number
def pickup_info():
    question = ("Please enter your name ")
    customer_details['name'] = not_blank(question )
    print (customer_details['name'])

    question = ("Please enter your phone number ")
    customer_details['phone'] = not_blank(question )
    print (customer_details['phone'])

#Delivery Information - Name, Phone number, House number, Street name, Suburb
def delivery_info():
    question = ("Please enter your name ")
    customer_details['name'] = not_blank(question )
    print (customer_details['name'])

    question = ("Please enter your phone number ")
    customer_details['phone'] = not_blank(question )
    print (customer_details['phone'])

    question = ("Please enter your house number ")
    customer_details['house'] = not_blank(question )
    print (customer_details['house'])

    question = ("Please enter your street name ")
    customer_details['street'] = not_blank(question )
    print (customer_details['street'])

    question = ("Please enter your suburb ")
    customer_details['suburb'] = not_blank(question )
    print (customer_details['suburb'])
    
    










































#Main Function
def main():
    '''
    Purpose: To generate a random name from the list and print out a welcome message
    Parameters: none
    Returns: none
    '''
    welcome()
    del_pick = order_type()

main()