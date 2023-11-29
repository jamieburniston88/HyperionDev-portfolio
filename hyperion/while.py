'''Initialise a variable as an empty list, 
stores the numbers inputted by the user'''
numbers = []
num = 0

while num != -1:  #checks if the value stored in the variable is not equal to -1.
    num = float(input("Enter a number (enter -1 to stop): "))
    if num != -1:
        numbers.append(num)
        
'''Calculates the average inputted numbers excluding -1 and displays the results'''      
if numbers:
    average = sum(numbers) / len(numbers)
    print(f"The average of the entered numbers is: {average}")
else:
    print("No numners were entered.")