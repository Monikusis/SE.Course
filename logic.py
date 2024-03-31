# Write a program that displays a logical error 

num = 5
if num > 0 and num == 0:
    print("Number is positive")
else:
    print("Number is negative")

"""
Code will always output False
Num can't be both greater than zero and equal to zero at the same time
This will print 'Number is negative' for any value of 'num'
"""
