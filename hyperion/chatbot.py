
'''Creating a chatbot to register a user's shopping budget and this will
assist in managing their budget, calculating remaining funds, 
and warning if they've overspent '''

# Ask the user for their total budget
total_budget = float(input("Enter your total budget: £"))

# Create an empty dictionary to store items and their prices
shopping_list = {}

# Ask user to input items and their respective prices until they're done
while True:
    item = input("Enter the item (or 'done' to finish adding items):")
    if item.lower()== 'done':
        break
    price = float(input(f"Enter the price of {item}: £"))
    shopping_list[item] = price
    total_budget -= price # Deducting the price from the total budget
    
# Check if the user has overspent
if total_budget < 0:
    print("Warning: You have overspent!")
    
# Display the items and remaining budget
print("\nYour shopping list:")
for item, price in shopping_list.items():
    print(f"{item}: £{price}")
    
print(f"\nRemaining budget: £{total_budget:.2f}") 