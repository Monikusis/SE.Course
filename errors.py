# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.
#HINT, 330 months is the correct answer


print("Welcome to the error program") # Missing parentheses for the sentence - syntax error.
print("\n") # Unnecessary indent, missing parentheses - syntax error.

# Unnecessary indent for code block below (IdentationError) - syntax error

# Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24" # 1.Remove 'years old' as it repeats in sentence. 2.Change == to =, as it's variable - syntax error
age = int(age_Str) 
print("I'm" + " " + str(age) + " " + "years old.") # Convert age to str, add spaces for user view - syntax error

# Variables declaring additional years and printing the total years of age
years_from_now = "3"
total_years = age + int(years_from_now) # Convert str to int - runtime error, code is running but not giving the right output 

print("The total number of years:", total_years) # Add missing parentheses, remove quatation from variable, change variable to tatal_years, add missing comma.
                                                 # Syntax errors - misspelling, leaving out important symbol, leaving out a keyword 

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = total_years * 12 + 6 # 1. Add 6 as per sentence below - runtime error. 2. Correct variable to total_years - syntax error, mispelling 
print("In 3 years and 6 months, I'll be ", total_months, "months old") # Add missing parentheses and comma - syntax error

