"""
write code to output the star pattern
using if-else statement 
in combination with a single for loop

*
**
***
****
*****
****
***
**
*

"""
rows = 5

for num in range(1, 2 * rows):
    if num <= rows:
        print("*" * num)
    else:
        print("*" * (2 * rows - num))