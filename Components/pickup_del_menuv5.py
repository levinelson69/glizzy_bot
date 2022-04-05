# Menu so that the user can choose either pickup or delivery
# Parameters: none
# Returns: none
print ("Is your order for Pickup or would you like it for Delivery?") #Asks the user if they would like thier order for pickup or delivery
print ("For Pickup please enter 1") #If the user would like pickup, they must input 1
print ("For Delivery please enter 2") #If the user would like delivery, they must input 2
while True: # Sets up while loop
    try: #checking the code for errors
        delivery = int(input("Please enter a number ")) # Input for the user to enter a number between 1 or 2
        if delivery >= 1 and delivery <= 2: #If statement for if the input is between 1 and 2
            if delivery == 1: #If 1 is entered print Pickup statement
                print ("Pickup")
                break # To break out of the loop

            elif delivery == 2: #If 2 is entered print Delivery statement
                print ("Delivery")
                break #To break out of the loop
        else: #If the integer input is not a 1 or a 2, print error statement
            print("Number must be 1 or 2")
    except ValueError: #If input is not a number, print error statement
        print("That is not a valid number")
        print("Please enter 1 or 2")