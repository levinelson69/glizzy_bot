sausage_names = ['Beef', 'Chicken', 'Pork', 'Cheese filled Pork', 'Spicy Pork', 'Venison', 'Peeled Pork', 'Authetic Bratwurst', 
                'Blood', 'Italian', 'Enormous Pork', 'World famous pork sausage within a pork Sausage']

sausage_prices = [3.50, 3.50, 3.50, 3.50, 3.50, 3.50, 3.50, 4.50, 4.50, 4.50, 6.00, 6.00]

def menu():
    number_sausages = 12

    for count in range (number_sausages):
        print("{} {} ${:.2f}" .format(count+1,sausage_names[count],sausage_prices[count]))

menu()
    
    
