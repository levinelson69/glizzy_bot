# Glizzy bot program

# Known Bugs
# 11/04/22 - Final printout is not printing customer details correctly
# 12/04/22 - If order is for pickup, you cannot cancel the order

import random
from random import randint
import sys
# Stored Constants so any function is able to use Low and High parameters
LOW = 1  # LOW equals 1
HIGH = 2  # HIGH equals 2
PH_LOW = 7  # PH_LOW equals 7
PH_HIGH = 10  # PH_HIGH equals 10
# List of random names
names = ["Mickey", "Nate", "Jay", "Jess", "Sally",
         "Annie", "Christopher", "Jake", "Nasal", "Betty"]
# List of Sausage names
sausage_names = ['Beef', 'Chicken', 'Pork', 'Cheese filled Pork',
                 'Spicy Pork', 'Venison', 'Peeled Pork', 'Authetic Bratwurst',
                 'Blood', 'Italian', 'Enormous Pork',
                 'World famous pork sausage within a pork Sausage']
# List of Sausage prices
sausage_prices = [3.50, 3.50, 3.50, 3.50, 3.50, 3.50,
                  3.50, 4.50, 4.50, 4.50, 6.00, 6.00]
# list to store ordered pizzas
order_list = []
# list to store pizza prices
order_cost = []


# Welcomes the user to the BOT with a randomized name
def welcome(): #Defining the welcome function used in main
    '''
    Purpose: To generate a random name from the list and
    print out a welcome message
    Parameters: none
    Returns: none
    '''
num = randint(0, 9)  # The num variable is what the program chooses as random number from 0 to 9
name = (names[num])  # The name varible is a random name from the list of random names and the num variable
print("*** Hi there and Welcome to Mickeys Glizzys! ***")  # Print statement welcome title, welcoming the user to the bot
print("*** My name is", name, "***")  # Print statement "my name is" and the random name variable 
print()  # Spacing between my print statements
print("I will be here to help you to order your hot and ready Sausages :)")  # Print statement of a friendly introduction of what the bot is for 
# customer details dictonary
customer_details = {}


# Validates inputs to check if they are blank
# Takes question as a parameter
# Returns response in title class if valid
def not_blank(question):  # Defining not blank function with question as a parameter
    valid = False  # Valid variable equals false
    while not valid:  
        response = input(question)
        if response != "":  # If the response is blank
            return response  # Return the response back to the top 
        else:  
            print("This cannot be blank")  # Print statement telling the user that their input cannot be blank


def check_string(question):  # Defining the check string function to check if the input for name questions only consist of letters
# Definces code as check_string with question as parameter
    while True:  # Sets up a loop
        response = input(question)  # Asks for input (string)
        x = response.isalpha()
        if x == False:  # if x is False prints error message
            print("Input must only contain letters")  #Print statement telling the user that their input cannot be blank
        else:
            return response.title()  # if True returns response in title class


# Validates inputs to check if they an integer
# Takes question as parameter
def val_int(low, high, question):  # Defines code as val_int with low, high and question as parameter
    while True:  # Sets up loop
        try:  # While the function is true 
            num = int(input(question))  # Asks the question
            if num >= low and num <= high:  # If input is greater or equal to low (1) and less than or equal to high (2)
                return num  # Returns and accepts the input
            else:  # If input is not the above
                print(f"Please enter a number between {low} and {high} ")  # Print statement telling the user that the input number must be between two values (1 and 2)
        except ValueError:
            print("That is not a valid number")  # Print statement telling the user that their input was not a valid number
            print(f"Please enter a number between {low} and {high} ")  # Print statement telling the user that input number must be between the 2 values (1 and 2)

# Validates input to check if they are a number
# Takes question as parameter
def check_phone(question, PH_LOW, PH_HIGH):  # Defines code as check_phone with question, PH_LOW, PH_HIGH as parameter
    while True:  # Sets up loop
        try:  # While the function is true
            num = int(input(question))  # Asks question as parameter
            test_num = num  # Input equals variable
            count = 0  # Count set as 0
            while test_num > 0:  # While input is greater than 0
                test_num = test_num//10  # test_num is equal to test_num divided by 10
                count = count + 1  # Adds 1 to count
            if count >= PH_LOW and count <= PH_HIGH:  # If count is greater or equal to PH_LOW and less than or equal to PH_HIGH
                return str(num)  # Returns and accepts input
            else:  # If input is not the above
                print("NZ phone numbers have between 7 and 10 digits")  # Print statement telling the user that their input must be between 7 and 10 digits
        except ValueError:
            print("Please enter a number")  # Print statement asking the user to input a 7-10 digit number

# Menu so that the user can choose either pickup or delivery
def order_type():  # Defining the order_type function
    '''
    Purpose: To create a menu for the user to choose pickup or delivery
    Parameter: none
    Return: return if del_pick is valid
    '''
    del_pick = ""  # del_pick variable equals nothing
    question = (f"Enter a number between {LOW} and {HIGH}: ")  # Question variable is a string that is used when the program must ask the user to enter a number between two numbers
    print()  # Spacing between my print statements
    print ("Would you like your order to be picked up or would you like it delivered?")  # Print statement asking the user how they would like their order arranged to be picked up or delivered
    print()  # Spacing between my print statements
    print ("For pickup please enter the number 1")  # Print statement telling the user to enter the number one if they would like to pick up their order
    print()  # Spacing between my print statements
    print ("For delivery please enter the number 2")  # Print statement telling the user to enter the number two if they would like their order delivered
    print()  # Spacing between my print statements
    delivery = val_int(LOW, HIGH, question)
    if delivery == 1:  # If the inputted number is 1
        print ("**Pickup**")  # Print statement telling the user that they have made an order for pickup
        del_pick = "pickup"
        pickup_info()  # Moves from current function to pickup info function
    else:  # Else/if the inputted number was a 2
        print ("**Delivery**")  # Print statement telling the user that they have made an order for delivery
        print()  # Spacing between my print statements
        print ("**You must pay an additional $9.00 Delivery Charge if you order 5 or less sausages")  # Print statement telling the user that they must pay a $9 delivery charge
        print()  # Spacing between my print statements
        delivery_info()  # Moves from current function to delivery info function
        del_pick = "delivery"  # del_pick equals delivery
    return del_pick  # Returns and accepts inputs


# Pickup Information - Name and Phone number
def pickup_info():  # Defined delivery info function used if the user chose their order type as delivery
    '''
    purpose: To collect users information 
    parameter: none
    return: none
    '''
    question = ("Please enter in your name ") # Question varible used by the user to input their name
    customer_details['name'] = check_string(question )  # Name input is checked by the check string function to see if the input only consists of letters
    print (customer_details['name'])  # Prints the user's inputted name and adds that to the customer details dictionary

    question = ("Please enter in your phone number ")  # Question varible used by the user to input their phone number
    customer_details['phone'] = check_phone(question, PH_LOW, PH_HIGH)  # Phone number is checked by the check phone function to see if the input only consists of numbers and the input is between 7 and 10 digits
    print (customer_details['phone'])  # Prints the user's inputted phone number and adds that to the customer details dictionary


# Delivery Information - Name, Phone number, House number, Street name, Suburb
def delivery_info():  # Defined delivery info function used if the user chose their order type as delivery
    '''
    purpose: To collect users information 
    parameter: none
    return: none
    '''
    question = ("Please enter in your name ")  # Question varible used by the user to input their name
    customer_details['name'] = check_string(question )  # Name input is checked by the check string function to see if the input only consists of letters
    print (customer_details['name'])  # Prints the user's inputted name and adds that to the customer details dictionary

    question = ("Please enter in your phone number ")  # Question varible used by the user to input their phone number
    customer_details['phone'] = check_phone(question, PH_LOW, PH_HIGH)  # Phone number is checked by the check phone function to see if the input only consists of numbers and the input is between 7 and 10 digits
    print (customer_details['phone'])  # Prints the user's inputted phone number and adds that to the customer details dictionary

    question = ("Please enter in your house number ")  # Question varible used by the user to input their house number
    customer_details['house'] = not_blank(question )  # House number input is checked by the not blank function to see if the input was left not blank
    print (customer_details['house'])  # Prints the user's inputted house number and adds that to the customer details dictionary

    question = ("Please enter in your street name ")  # Question varible used by the user to input their street name
    customer_details['street'] = check_string(question )   # Street input is checked by the check string function to see if the input only consists of letters
    print (customer_details['street'])  # Prints the user's inputted street name and adds that to the customer details dictionary

    question = ("Please enter in your suburb ")  # Question varible used by the user to input their suburb
    customer_details['suburb'] = check_string(question )   # Suburb input is checked by the check string function to see if the input only consists of letters
    print (customer_details['suburb'])  # Prints the user's inputted suburb and adds that to the customer details dictionary


# Sausage Menu
def menu():  # Defining the menu function
    '''
    purpose: To print the sausage menu
    paramater: none
    return: none
    '''
    number_sausages = 12  # Number of sausages variable equals 12

    for count in range(number_sausages):  # For sausages ranged between 1 and 12
        print("{} {} ${:.2f}" .format(count+1, sausage_names[count], sausage_prices[count]))  # Print the sausages on the menu in a list from 1 to 12 with the correct prices next to each sausage with a dollar sign and within 2 decimal places


def order_sausage():  # Defining the order sausage function
    '''
    purpose: Ask user how many sausages they want to order
    parameter: none
    return: none
    '''
    # ask for total number of sausages for order
    num_sausages = 0
    LOW = 1  # Low constant for this particular function equals 1
    HIGH = 8  # High constant for this particular function equals 8
    MENU_LOW = 1  # Menu Low constant equals 1
    MENU_HIGH = 12  # Menu High constant equals 12
    question = (f"Enter a number between {LOW} and {HIGH} ")  # Question variable asking the user to enter a number between two values (1 and 8)
    print()  # Spacing between my print statements
    print("How many sausages delicious sausages would you like to order?")  # Print statement asking the user how many sausages they want to order
    print()  # Spacing between my print statements
    num_sausages = val_int(LOW, HIGH, question)  # Input for the number of sausages is checked using the val int function to check if the input on consisted of numbers 

    # Choose sausage from menu
    for item in range(num_sausages):
        while num_sausages > 0:  # While the number of sausages wanted is greater than 0
            print()  # Spacing between my print statements
            print("Please choose your sausages by entering the number from the yummy sausage menu ")  # Print statement telling the user to choose a sausage from the menu by entering a number from 1 to 12
            print()  # Spacing between my print statements
            question = (f"Enter a number between {MENU_LOW} and {MENU_HIGH} ")  # Asks user to enter a number between two values (1 and 12)
            sausage_ordered = val_int(MENU_LOW, MENU_HIGH, question)  #Sausage ordered equals validated input
            sausage_ordered = sausage_ordered - 1  # sausage ordered equals validated input minus 1
            order_list.append(sausage_names[sausage_ordered])  # Sausage names are added to order list
            order_cost.append(sausage_prices[sausage_ordered])  # Sausage prices are added to order list
            print("{} ${:.2f})" .format(sausage_names[sausage_ordered], sausage_prices[sausage_ordered]))  # Print statement of ordered sausages with prices
            num_sausages = num_sausages - 1  # num_sausage equals num_sausage minus 1


# Print order out - including if order is del or pickup
# and names of each pizza - total cost including any delivery charge
def print_order(del_pick):  # Defines function as print_order(del_pick) with parameter
    '''
    purpose: To print the customers order
    parameter: del_pick
    return: none
    '''
    total_cost = sum(order_cost)  # The total cost of the order is the sum of the order cost 
    print ("Customer Details")  # Print statement title for the user's customer details
    if del_pick == "pickup":  # If order type is for pickup
        print("Your order is for **Pickup**")  # Print statement telling the user that their order was for pickup
        print()  # Spacing between my print statements
        print(f"Customer Name: {customer_details['name']} \nCustomer Phone: {customer_details['phone']}")  # Print statement of all the customer's details entered when they chose Pickup
        print()  # Spacing between my print statements

    elif del_pick == "delivery":  # If order type is for delivery
        print()  # Spacing between my print statements
        print("Your order is for **Delivery**")  # Print statement telling the user that their order is for delivery
        if len(order_list) >= 5:  # If number of Sausages ordered is more than or equal to 5
            print ("Your order will be delievered for free")  # Prints message informing the customer their delivery fee is free
        elif len(order_list) < 5:  # If number of Sausages ordered is less than 5
            print ("There is an additional $9.00 delivery charge")  # Print statement telling the user that there will be a $9.00 delivery fee
        total_cost = total_cost + 9  # The total cost of the order is the total cost + $9.00 for the delivery fee
        print()  # Spacing between my print statements
        print(f"Customer Name: {customer_details['name']} \nCustomer Phone: {customer_details['phone']} \nCustomer Address: {customer_details['house']} {customer_details['street']} {customer_details['suburb']}")  # Print statement of all the customer's details entered when they chose delivery
        print("A $9.00 Delivery charge applies")  # Print statement telling the user that there is a $9.00 delivery fee 
    print()  # Spacing between my print statements
    print("Your Order Details")  # Print statement title for the user's order details
    print()  # Spacing between my print statements
    count = 0  # Set count to zero
    for item in order_list:  # For items in order list
        print()  # Spacing between my print statements
        print("Ordered: {} Cost ${:.2f}".format(item, order_cost[count]))  # Print the order deatils in the order they were ordered and with the correct prices of that sausage with a dollar sign and within 2 decimal places
        count = count+1  # Count equals count plus 1
    print()  # Spacing between my print statements
    print("Total Order Cost")  # Print statement title of the total order cost
    print(f"${total_cost:.2f}")  # Print statement of the total order cost with a dollar sign and within 2 decimal places


# Confirm order or cancel
def cancel_confirm(del_pick):  # Defines the following function as cancel_confirm
    '''
    purpose: To give the user the option to cancel or confirm thier order
    parameter: none
    return: none
    '''
    question = (f"Enter a number between {LOW} and {HIGH} ")  # Question variable telling the user to enter a number between 2 values (1 and 2)
    print()  # Spacing between my print statements
    print ("Please Confirm Your Order")  # Print statement telling the user to confirm their order
    print()  # Spacing between my print statements
    print ("For confirm please enter the number 1")  # Print statement telling the user thet can confirm their order by entering the number 1
    print()  # Spacing between my print statements
    print ("For cancel please enter the number 2")  # Print statement telling the user they can cancel their order by entering the number 2
    print()  # Spacing between my print statements
    confirm = val_int(LOW, HIGH, question)  # Confirm equals validated input
    if confirm == 1:  # If the user inputted 1
        print ("**Order Confirmed**")  # Print statement telling the user their order has been confirmed
        new_exit()  # So the program moves on to the new exit function
    if del_pick == "pickup" and confirm == 1:  # If input equals 2
        print("You will be sent a text message when your order is ready to be picked up")  # Print statement telling the user that they will recieve a message when their order is ready
        new_exit()  # So the program moves on to the new exit function
    elif confirm == 2:  # if the user inputted 2
        print ("**Order Cancelled**")  # Print statement telling the user their order has been cancelled
        print ("You may restart your order or exit the BOT")  # Print statement telling the user that they may still restart their order or exit the bot
        new_exit()  # So the program moves on to the new exit function


# Option for new order
def new_exit():  # Defines the following function as new_exit
    '''
    purpose: To give the user the ability to start a new order or exit the bot
    parameter: none
    return: none
    '''
    question = (f"Enter a number between {LOW} and {HIGH} ")  # Question variable telling the user to enter a number between 2 values (1 and 2)
    print()  # Spacing between my print statements
    print ("Would you like to place another Order or Exit?")  # Print statement asking the user if they would like to place another order/restart or exit the bot
    print()  # Spacing between my print statements
    print ("To place another order please enter the number 1")  # Print statement telling the user they can place another order/restart order by entering the number 1
    print()  # Spacing between my print statements
    print ("To exit the BOT please enter the number 2")  # Print statement telling the user they can exit the bot by entering the number 2
    print()  # Spacing between my print statements
    confirm = val_int(LOW, HIGH, question)
    if confirm == 1:  # If input equals 1
        print ("New Order")  # Print statement title of new order, telling the user that they have just started a new order
        order_list.clear()  # Clearing information off all previous lists
        order_cost.clear()  # Clearing information off all previous lists
        customer_details.clear()  # Clearing information off all previous lists
        main()  # Running the main function again after all lists have been cleared (Placing a new order or restarting order from the beginning)

    elif confirm == 2:  # Else if confirm input equals 2
        print ("Exit")   # Print statement title of exit, telling the user that they have exited the bot and can no longer add anymore information
        order_list.clear()  # Clearing information off all previous lists
        order_cost.clear()  # Clearing information off all previous lists
        customer_details.clear()  # Clearing information off all previous lists
        sys.exit()  # System exits (user exits out of the program)


# Main Function
# Defining my main function that
# consists of all my other created functions
def main(): 
    '''
    Purpose: To run all functions
    Parameters: None
    Returns: None
    '''
    welcome()  # The welcoming function used in my program
    del_pick = order_type()  # The order tyoe function used in my program and a part of the del pick variable
    menu()  # The menu function used in my program
    order_sausage()  # The ordering of sausages function used in my program
    print_order(del_pick)  # The order being printed function used in my program in correspondence to the del pick parameter
    cancel_confirm(del_pick)  # The canceling or confirming function used in my program in correspondence to the del pick parameter
main()
