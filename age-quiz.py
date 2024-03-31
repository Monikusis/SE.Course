# Input for a user 

age = int(input("Please enter your age: "))

# Outputs for responses

if age >= 40 and age <65:
    print("You're over the hill.")
elif age > 100:
    print("Sorry, you are dead.")
elif age >= 65:
    print("Enjoy your retirement!")
elif age < 13:
    print("You qualify for the kiddie discount.")
elif age == 21:
    print("Congrats on your 21st!")
else:
    print("Age is but a number")


