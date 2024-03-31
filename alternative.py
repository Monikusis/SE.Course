"""
1. Write a program that reads in string 
and makes each alternate CHARACTER into an upper case
and each other alternate character a lower case character 
e.g. The string "Hello World" would become "HeLlO WoRlD"

2. Same string to make each alternative word lower and upper
e.g. "I am learning to code" becomes "i AM learning TO code."

Hint : use split() and join()
"""

# Changing each alternative character to upper case
def alternate_char_case(input_string):
    result = ""
    for i, char in enumerate(input_string):
        if i % 2 == 0:
            result += char.upper()
        else:
             result += char.lower()
    return result

#Read a string from user input 
user_input = input("Enter a string: ")

#Apply conversion to input 
converted_string = alternate_char_case(user_input)

print("Alternate character changed to upper case: ", converted_string)

# Changing each alternative word to upper case
def alternate_word_case(input_string):
    words = input_string.split()
    result = " "
    for i, word in enumerate(words):
        if i % 2 == 0:
            result += word.lower()
        else:
            result += word.upper()
        result += " "
    return result.strip()

#Apply word conversion to input
converted_words = alternate_word_case(user_input)
print("Alternate word changed to upper case:", converted_words)

