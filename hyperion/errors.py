# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

''' syntax errors added the () and rewmoved the tab space'''
print("Welcome to the error program")
print("\n")

    # Variables declaring the user's age, casting the str to an int, and printing the result
''' syntax errors, removing extra "="
Runtime errors, adding str() for concaternations, added .split() to extract numerical value from the string'''
age_str = "24 years old" 
age = int(age_str.split()[0]) 
print("I'm " + str(age) + " years old.") 

    # Variables declaring additional years and printing the total years of age
''' syntax errors removing unneccassary "" and adding ()
runtime errors adding str() to help concatenation
Logical errors changed "answer_years" to "total_years"'''
years_from_now = 3 
total_years = age + years_from_now
print("The total number of years:" + str(total_years))  

# Variable to calculate the total amount of months from the total amount of years and printing the result
''' Syntax errors added ()
Logical Errors adding "+ 6" too reach 330 months as this is stated in the string'''
total_months = total_years * 12 + 6 
print("In 3 years and 6 months, I'll be " + str(total_months) + " months old")

#HINT, 330 months is the correct answer

