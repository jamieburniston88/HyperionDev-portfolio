'''Pseudocode
1. Save the sentence into a variable
2. create new variable and use string method .replace() "!" to " "
3. Use print() on new variable to show replaced phrase
4. Create new variable and use string method .upper() 
5. Use print() on new variable to show uppercased phrase
6. Create new variable and use slice method [::-1]
7. Use print() on new variable to show reversed phrase'''








phrase = "The!quick!brown!fox!jumps!over!the!lazy!dog."
replaced_phrase = phrase.replace("!", " ")
print(replaced_phrase)

uppercase_phrase = replaced_phrase.upper()
print(uppercase_phrase)

reversed_phrase = phrase[::-1]
print(reversed_phrase)