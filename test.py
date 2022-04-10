# Pizza Bot Program
#Bugs - Phone number input allows letters
#Name input allows numbers


import sys
import random
from random import randint

#List of random names
names = ["Ross" , "Poppy" , "Joe" , "Sandy" , "Ben" , "Marisa" , "Steve" , "Susie" , "Jacob" , "Ziniac"]
# List of pizza names
pizza_names = ['Margherita','Pepperoni','Hawaiian','Cheese','Italian','Veggie','Vegan','Chicken Deluxe',
                'Mega Meat Lovers','Seafood Deluxe','Apricot Chicken Deluxe','BBQ Chicken Deluxe']
# List of pizza prices
pizza_prices = [8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 13.50, 13.50, 13.50, 13.50, 13.50]

#list to store ordered pizzas
order_list = []
#list to store pizza prices
order_cost = []

#Customer details dictonary 
customer_details = {}
# Validates inputs to check if they are blank
def not_blank(question):
    valid = False
    while not valid:
        response = input(question)
        if response != "":
            return response.title()
        else:
            print("This cannot be blank")




# Menu for pickup or delivery
def welcome():
    '''
    Purpose: To generate a random name from the list and print out a welcome message
    Parameters: none
    Returns: none
    '''
    
    num = randint(0,9)
    name = (names[num])
    print("*** Welcome to Dream Pizza ***")
    print("*** My name is",name, "***")
    print("I will be here to help you to order your delicious Dream Pizza")


# Menu for pickup or delivery
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

# Pick Up information - name and phone number
def pickup_info():
    question = ("Please enter your name ")
    customer_details['name'] = not_blank(question )

    question = ("Please enter your phone number ")
    customer_details['phone'] = not_blank(question )
    print(customer_details)


# Delivery information - name, address and phone

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
