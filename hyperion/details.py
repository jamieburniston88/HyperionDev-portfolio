'''Pseudocode:
1. Prompt user to input their name using variable
2. Read the input using input()
3. Prompt user to input their age using variable
4. Read the input using input()
5. Prompt user to input their house number using variable
6. Read the input using input()
7. Prompt user to input their street name using variable
8. Read the input using input()
9. Create variable details with text that shows the users inputs using .format
3. Print(details.format)
'''

name = input("Please enter your name: ")

age = input("Please enter your age: ")

house_number = input("Please enter your house number: ")

street_name = input("Please enter your street name: ")

details = "This is {0}. He is {1} years old and lives at house number {2} on {3}."
print(details.format(name, age, house_number, street_name))
