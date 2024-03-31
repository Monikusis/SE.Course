import math

"""
Create a program that continually ask user to enter a number 
Stop requesting when enter -1 
Calculate the average of numbers entered except -1 
"""

numbers = []
while True:
    
    user_number = int(input("Please enter your number: "))

    if user_number == -1:
        break

    numbers.append(user_number)

if numbers:
    average = sum(numbers) / len(numbers)
    print("The average is: ", average)
        

