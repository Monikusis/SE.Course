# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion" # Name is not defined, added quotation - syntax error 
animal_type = "cub"
number_of_teeth = 16

full_spec = f"This is a {animal}. It is a {number_of_teeth} and it has {animal_type} teeth" # Add f-string to format the string with valuables
# Runtime error - code is running but variambles are not being exported in output. 

print(full_spec) # Missing parentheses - syntax error 