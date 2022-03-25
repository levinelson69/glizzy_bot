# Menu so that the user can choose either pickup or delivery
#Bug: Must make program so it only accepts 1 or 2

print ("Is your order for Pickup or would you like it for Delivery?")

print ("For delivery please enter 1")
print ("For pickup please enter 2")


low = 1
high = 2

while True:
    try:
        delivery =int(input("Please enter a number"))

        if delivery == 1:
            print ("Pickup")
            break          

        elif delivery == 2:
            print ("Delivery")
            break
    
    except ValueError:
        print("**That is not a valid number**")
        print("Please enter 1 for Pickup or 2 for Delivery")

