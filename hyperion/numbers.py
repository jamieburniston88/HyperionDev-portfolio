'''Pseudo code
1. Ask user to enter three different integers using integer & input() method.
2. Calculate and print through the sum_all function
3. Find tghe difference through the mathematical equations'''

num1 = int(input("Enter a integer: "))
num2 = int(input("Enter a integer: "))
num3 = int(input("Enter a integer: "))
           
sum_all = num1 + num2 + num3
print("Sum of all numbers:", sum_all)

difference = num1 - num2
print("First number minus second number equals: ", difference)

multiplication = num3 * num1
print("Third number times first number equals: ", multiplication)

division = sum_all / num3
print("Sum of all three numbersdivided by the third number equals: ", division)

