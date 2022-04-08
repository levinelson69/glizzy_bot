from Glizzy_bot import pickup_info, delivery_info


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

