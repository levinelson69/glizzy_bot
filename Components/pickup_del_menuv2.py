# Bugs
#Will only work for valid input "d" and "p"

# Menu so that the user can choose either pickup or delivery
#When input is invalid, else statement is triggered but program does not ask for another input

print ("Do you want your order delivered or are you picking it up?")

print ("For delivery enter d")
print ("For pickup please enter p")

delivery = input()

if delivery == "d":
    print ("Delivery")

elif delivery == "p":
    print ("Pickup")

else:
    print("**That was not a valid input**")