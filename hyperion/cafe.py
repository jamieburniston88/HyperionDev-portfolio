# Menu list 
menu = (['Coffee', 'Sandwich', 'Cake', 'Tea' ])

# Stock Dictionary
stock = {
    'Coffee': 50,
    'Sandwich': 20,
    'Cake': 15,
    'Tea': 30
}

# Price Dictionary
price = {
    'Coffee': 2.5,
    'Tea': 1.8,
    'Sandwich' : 5.0,
    'Cake' : 3.5
}

#Calculating total stock worth
total_stock_worth = 0
for item in menu:
    item_value = stock[item] * price[item]
    total_stock_worth += item_value
    
print(f"The total stock worth in the cafe is: £{total_stock_worth:.2f}")