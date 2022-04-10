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

# Ask for total number of sausages ordered
num_sausage = 0

num_sausage = int(input("How many sausages do you want to order? "))

print(num_sausage)

# Choose Sausage from 
print ("Choose your sausages by entering the number from the menu")
for item in range(num_sausage):
    while num_sausage > 0:
        sausage_ordered = int(input())
        order_list.append(sausage_names[sausage_ordered])
        order_cost.append(sausage_prices[sausage_ordered])
        num_sausage = num_sausage-1

print(order_list)
print(order_cost)
# Countdown until all sausages are ordered

# Print order




