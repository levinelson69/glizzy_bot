# Bugs
#Will only work for valid input "1" and "2"

# Menu so that the user can choose either pickup or delivery
#When input is invalid, else statement is triggered but program does not ask for another input

print ("Is your order for Pickup or would you like it for Delivery?")

print ("For delivery please enter 1")
print ("For pickup please enter 2")



delivery =int(input())

if delivery == "1":
    print ("Delivery")
         

elif delivery == "2":
    print ("Pickup")

else:
   print ("**That was not a valid input**")

    

