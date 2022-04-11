#list to store ordered sausagess
order_list = ['Beef', 'Pork', 'Blood', 'Italaian']
#list to store pizza prices
order_cost = [3.50, 3.50, 4.50, 4.50]

cust_details = {'name':'Levi','phone':'0217612487', 'house':'78', 'street':'Joe', 'suburb':'Idk'}



print("\n Customer Name: {} Customer Phone:\n{} Customer House Number:\n{} Customer Street Name:\n{} Customer Suburb:\n{}".format( cust_details['name'],cust_details['phone'],cust_details['house'],cust_details['street'],cust_details['suburb']))

count = 0
for item in order_list:
    print("Ordered: {} Cost ${:.2f}".format(item, order_cost[count]))
    count = count+1