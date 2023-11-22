'''Pseudo code
1. Create a variable named age, use int() and input() method to capture user data
2. Create if/elif/else statement for various age ranges
3. Use the comparative operators to create greater/less/equals to
4. Set up conditions into a logical order for the logical tests to be applied'''



age = int(input("Please enter your age: "))
if age <= 13:
    print("You qualify for the kiddie discount.")
elif age == 21:
    print("Congrats on your 21st.")
elif age > 100:
    print("Sorry, you'er dead")
elif age >= 65:
    print("Enjoy your retirement!")
elif age >= 40:
    print("You're over the hill.")
else:
    print("Age is but a number.")