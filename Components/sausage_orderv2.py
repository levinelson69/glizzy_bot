# List of Sausage names
sausage_names = ['Beef', 'Chicken', 'Pork', 'Cheese filled Pork', 'Spicy Pork', 'Venison', 'Peeled Pork', 'Authetic Bratwurst', 
                'Blood', 'Italian', 'Enormous Pork', 'World famous pork sausage within a pork Sausage']
# List of sausage prices
sausage_prices = [3.50, 3.50, 3.50, 3.50, 3.50, 3.50, 3.50, 4.50, 4.50, 4.50, 6.00, 6.00]
# List to store ordered Sausages
order_list =[]
# List to store Sausage prices
order_cost = []
#List to store order cost

def menu():
    number_sausages = 12

    for count in range(number_sausages):
        print("{} {} ${:.2f}" .format(count+1,sausage_names[count],sausage_prices[count]))

menu()

# ask for total number of sausages for order
num_sausage = 0

while True:
    try:
        num_sausage = int(input("How many sausages do you want to order? "))
        if num_sausage >= 1 and num_sausage <=8:
            break
        else:
            print ("Your order must be between 1 and 8")
    except ValueError:
        print ("That is not a valid number")
        print ("Please enter a number between 1 and 8")



#Choose sausage from menu
for item in range(num_sausage):
    while num_sausage > 0:
        while True:
            try:
                sausage_ordered = int(input("Please choose your sausages by entering the number from the menu "))
                if sausage_ordered >= 1 and sausage_ordered <= 12:
                    break
                else:
                    print ("Your order must be between 1 and 12")
            except ValueError:
                print ("That is not a valid number")
                print ("Please enter a number between 1 and 12")
        sausage_ordered = sausage_ordered -1
        order_list.append(sausage_names[sausage_ordered])
        order_cost.append(sausage_prices[sausage_ordered])
        print("{} ${:.2f})" .format(sausage_names[sausage_ordered],sausage_prices[sausage_ordered]))
        num_sausage = num_sausage-1

print(order_list)
print(order_cost)