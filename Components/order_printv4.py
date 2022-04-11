#list to store ordered sausagess
order_list = ['Beef', 'Pork', 'Blood', 'Italaian']
#list to store pizza prices
order_cost = [3.50, 3.50, 4.50, 4.50]

cust_details = {'name':'Levi','phone':'0217612487', 'house':'78', 'street':'Joe', 'suburb':'Idk'}

def print_order():
    total_cost = sum(order_cost)
    print ("Customer Details")
    print(f"Customer Name: {cust_details['name']} \nCustomer Phone: {cust_details['phone']} \nCustomer Address: {cust_details['house']} {cust_details['street']} {cust_details['suburb']}")
    print()
    print("Order Details")
    count = 0
    for item in order_list:
        print("Ordered: {} Cost ${:.2f}".format(item, order_cost[count]))
        count = count+1
    print()
    print("Total Order Cost")
    print(f"${total_cost:.2f}")

print_order()