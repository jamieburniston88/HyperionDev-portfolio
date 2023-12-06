def alternate_case(string):
# Initiate an empty string to store the result
    result = ""
    
# Loop through each character in the input string
    for i, char in enumerate(string):
# Check if thew character's index is even or odd
        if i % 2 == 0:
# Convert even characters to uppercase otherwise convert to lowercase
            result += char.upper()
        else:
            result += char.lower()
    return result

input_string = "Hello World"
output_string = alternate_case(input_string)
print(output_string)





def alternate_words_case(string):
# Split the input string into a list of words
    words = string.split()
    
# Initiate an empty string to store the results
    result = ' ' .join([words[i].lower() if i % 2 == 0 else words[i].upper() for i 
in range(len(words))])
# Iterate through the words, alternately converting them to lower or upper case based on their index

    return result

input_string = "I am learning to code"
output_string = alternate_words_case(input_string)
print(output_string)