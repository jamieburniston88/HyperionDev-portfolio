import math # imports modules that creates greater techniques into programming

def main():
#Creates welcome message and initial menu
    print("Welcome to the Finance Calculator!")
    print("investment - to calculate the amount of interest you'll earn on your investment")
    print("Bond - to calculate the amount you'll have to pay on a home loan")
    
# gets user choice and .lower converts any input to lowercase for consistency
    user_choice= input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()
    
    if user_choice == "investment": #if investment is chosen, call calculate_investment function
        calculate_investment()
    elif user_choice == "bond": #if bond is chosen, call calculate_bond function
        calculate_bond()
    else:
        print("Invalid input. Please choose 'investment' or 'bond'.")
        
#Function to calculate investment        
def calculate_investment():
    #Gathering user inputs
    amount = float(input("Enter the amount of money being deposited: "))
    interest_rate = float(input("Enter the interest rate(as a percentage): "))
    years = int(input("Enter the number of years for investment: "))
    interest_type = input("Enter 'simple' or 'compound' interest: ").lower()
    
    #Convert the interest rate to decimal
    interest_rate/= 100
    
    #Calculate based on interest type chosen
    if interest_type == "simple":
        total_amount = amount *(1 + interest_rate * years) # Calculate simple interest
    elif interest_type == "compound":
        # calculate compound interest, math.pow() method  returns the value of x raised to power y.
        total_amount = amount * math.pow((1 + interest_rate), years) 
    else:
        print("Invalid interest type. Please choose 'simple' or 'compound'.")
        return
    
    #Display the total amount after investment
    print(f"The total amount after {years} years will be: {total_amount:.2f}")
    
 #Function to calculate bond repayment   
def calculate_bond():
    #Gathering user inputs
    present_value = float(input("Enter the present value of the house: "))
    interest_rate = float(input("Enter the annual interest rate: "))
    months = int(input("Enter the number of months for the bond repayment: "))
    
    #Converts annual interest rate to monthly and then to decimal
    monthly_interest_rate = (interest_rate/ 100) / 12
    
    #Bond repayment calculation
    repayment = (monthly_interest_rate * present_value) / (1 - math.pow((1 + monthly_interest_rate), -months))
    
    #Displays the monthly repayment amount for the bond
    print(f"The monthly repayment amount for the bond is: {repayment:.2f}")
    
if __name__ == "__main__":
    main()