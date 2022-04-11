#list to store ordered sausagess
order_list = ['Beef', 'Pork', 'Blood', 'Italaian']
#list to store pizza prices
order_cost = [3.50, 3.50, 4.50, 4.50]

count = 0
for item in order_list:
    print("Ordered: {} Cost ${:.2f}".format(item, order_cost[count]))
    count = count+1
