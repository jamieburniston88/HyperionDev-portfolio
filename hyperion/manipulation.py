'''pseudo code
1. create variable str_manip and use input() to capture a user data
2. Using data collected from str_manip, use len() to state the sentence's length
3. Use slice method to print the sentences last letter in a new variable
4. Use the .replace method to replace last_letter with "@" 
5. Use the slice method to print last three words backwards and to create a 5 letter word'''

str_manip = input("Please enter a sentence ")

length = len(str_manip)
print("Length of str_manip:",length)

last_letter = str_manip[-1]
print(last_letter)

str_manip = str_manip.replace(last_letter,'@')
print(str_manip)

last_three_backwards = str_manip[-1:-4:-1]
print("Last three characters backwards:", last_three_backwards)

five_letter_word = str_manip[:3] + str_manip[-2:]
print("Five letter word: ", five_letter_word)