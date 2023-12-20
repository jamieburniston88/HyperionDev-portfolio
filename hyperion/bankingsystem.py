# Create random figures for the balance
import random as rd

# Creates random balance 
def check_bal():
    current_balance = rd.randint(100, 999999)
    return f"Your current balance is £{current_balance}"

user_credentials = {} # Store crendtials for user
user_balances = {}  # Store balances for users

def create_account():
    username = input("Enter a username: ")
    pin = input("Enter a 4-digit PIN: ")
    
    if username in user_credentials:
        print("Username already exists. Please choose a different username.")
    elif len(pin) != 4 or not pin.isdigit():
        print("Please enter a 4-digit PIN.")
    else:
        user_credentials[username] = pin
        user_balances[username] = rd.randint(100, 999999)  # Initialize balance
        print("Account created successfully!")

def login(max_attempt = 3):
    attempts = 0 # Creates control over the amount of attempts the user has to input correct deatils
    while attempts < max_attempt:
        
        username = input("Enter your username: ")
        pin = input("Enter your 4-digit PIN: ")
    
    if username in user_credentials and user_credentials[username] == pin:
        return True, username
    else:
        print("Invalid username or PIN. Please try again.")
        attempts += 1
    print("Maximum login attempts reached.")
    return False, None

# Initial account creation
create_account()

# Banking operations
while True:
    print("Welcome to the bank!")
    print("1. Check Balance")
    print("2. Transfer Funds")
    print("3. Deposit Money")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        authenticated, user = login()
        if authenticated:
            print(check_bal())
            break
    elif choice == "2":
        authenticated, user = login()
        if authenticated:
            recipient = input("Enter recipient's username: ")
            amount = float(input("Enter the amount to transfer: "))
            if recipient in user_balances:
                if user_balances[user] >= amount:
                    user_balances[user] -= amount
                    user_balances[recipient] += amount
                    print("Transfer successful!")
                else:
                    print("Insufficient funds.")
            else:
                print("Recipient username not found.")
        else:
            print("Please login with valid credentials.")
    elif choice == "3":
        authenticated, user = login()
        if authenticated:
            amount = float(input("Enter the amount to deposit: "))
            user_balances[user] += amount
            print("Deposit successful!")
        else:
            print("Please login with valid credentials.")
    elif choice == "4":
        print("Thank you for using the bank. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")

