# Glizzy bot program

# Known Bugs
# 11/04/22 - Final printout is not printing customer details correctly
# 12/04/22 - If order is for pickup, you cannot cancel the order

import sys
import random
from random import randint
# Constants
LOW = 1
HIGH = 2

# List of random names
names = ["Mickey", "Nate", "Jay", "Jess", "Sally", "Annie",
         "Christopher", "Jake", "Nasal", "Betty"]
# List of Sausage names
sausage_names = ['Beef', 'Chicken', 'Pork', 'Cheese filled Pork',
                 'Spicy Pork', 'Venison', 'Peeled Pork', 'Authetic Bratwurst', 
                 'Blood', 'Italian', 'Enormous Pork',
                 'World famous pork sausage within a pork Sausage']
# List of Sausage prices
sausage_prices = [3.50, 3.50, 3.50, 3.50, 3.50, 3.50, 3.50, 4.50, 4.50, 4.50, 6.00, 6.00]
# list to store ordered pizzas
order_list = []
# list to store pizza prices
order_cost = []

# Welcomes the user to the BOT with a randomized name
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
# customer details dictonary 
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

# Validates inputs to check if they an integer
def val_int(low, high, question):
    while True:
        try:
            num = int(input(question))
            if num >= low and num <= high:
                return num
            else:
                print(f"Please enter a number between {low} and {high} ")
        except ValueError:
            print("That is not a valid number")
            print(f"Please enter a number between {low} and {high} ")



# Menu so that the user can choose either pickup or delivery
def order_type(): # Defining the order_type function
    del_pick = ""
    question = (f"Enter a number between {LOW} and {HIGH}: ")
    print ("Is your order for pickup or delivery?")
    print ("For pickup please enter 1")
    print ("For delivery please enter 2")
    delivery = val_int(LOW, HIGH, question)
    if delivery == 1:
        print ("Pickup")
        del_pick = "pickup"
        pickup_info()
    else:
        print ("Delivery")
        print ("**You must pay an additional $9.00 Delivery Charge**")
        delivery_info()
        del_pick = "delivery"
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
def delivery_info(): #Defined function 
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
    
#Sausage Menu

def menu():
    number_sausages = 12

    for count in range (number_sausages):
        print("{} {} ${:.2f}" .format(count+1,sausage_names[count],sausage_prices[count]))

def order_sausage():
    # ask for total number of sausages for order
    num_sausages = 0
    NUM_LOW = 1
    NUM_HIGH = 8
    MENU_LOW = 1
    MENU_HIGH = 12
    question = (f"Enter a number between {NUM_LOW} and {NUM_HIGH} ")
    print()
    print("How many sausages do you want to order?")
    print()
    num_sausages = val_int(NUM_LOW, NUM_HIGH, question)

    #Choose sausage from menu
    for item in range(num_sausages):
        while num_sausages > 0:
            print("Please choose your sausages by"
            " entering the number from the menu ")
            question = (f"Enter a number between {MENU_LOW} and {MENU_HIGH} ")
            sausage_ordered = val_int(MENU_LOW, MENU_HIGH, question)
            sausage_ordered = sausage_ordered -1
            order_list.append(sausage_names[sausage_ordered])
            order_cost.append(sausage_prices[sausage_ordered])
            print("{} ${:.2f})" .format(sausage_names[sausage_ordered],sausage_prices[sausage_ordered]))
            num_sausages = num_sausages-1

#Print order out - including if order is del or pickup and names of each pizza - total cost including any delivery charge
def print_order(del_pick):
    total_cost = sum(order_cost)
    print ("Customer Details")
    if del_pick =="pickup":
        print("Your order is for Pickup")
        print(f"Customer Name: {customer_details['name']} \nCustomer Phone: {customer_details['phone']}")

    elif del_pick =="delivery":
        print("Your order is for Delivery")
        total_cost = total_cost + 9
        print(f"Customer Name: {customer_details['name']} \nCustomer Phone: {customer_details['phone']} \nCustomer Address: {customer_details['house']} {customer_details['street']} {customer_details['suburb']}")
        print("A $9.00 Delivery charge applies")
    print("Your Order Details")
    print("Delivery Fee $9.00")
    count = 0
    for item in order_list:
        print("Ordered: {} Cost ${:.2f}".format(item, order_cost[count]))
        count = count+1
    print("Total Order Cost")
    print(f"${total_cost:.2f}")

#Confirm order or cancel
def cancel_confirm(del_pick):
    question = (f"Enter a number between {LOW} and {HIGH} ")
    print ("Please Confirm Your Order")
    print ("For confirm please enter 1")
    print ("For cancel please enter 2")
    confirm = val_int(LOW, HIGH, question)
    if confirm == 1:
        print ("**Order Confirmed**")
        new_exit()
    if del_pick == "pickup" and confirm ==1:
        print("You will be sent a text message when your order is ready to be picked up")
        new_exit()
    elif confirm == 2:
        print ("**Order Cancelled**")
        print ("You may restart your order or exit the BOT")
        new_exit()


#Option for new order
def new_exit():
    question = (f"Enter a number between {LOW} and {HIGH} ")
    print ("Would you like to place another Order or Exit?")
    print ("To place another order please enter 1")
    print ("To exit the BOT please enter 2")
    confirm = val_int(LOW, HIGH, question)
    if confirm == 1:
        print ("New Order")
        order_list.clear()
        order_cost.clear()
        customer_details.clear()
        main()

    elif confirm == 2:
        print ("Exit")
        order_list.clear()
        order_cost.clear()
        customer_details.clear()
        sys.exit()

#Main Function
def main(): #Defining my main function that consists of all my other created functions
    welcome()
    del_pick = order_type()
    menu()
    order_sausage()
    print_order(del_pick)
    cancel_confirm(del_pick)
main()