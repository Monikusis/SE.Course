import math

"""
User needs to choose investment or bond 
If not valid show error message 
If selected investment, ask for input with questions 
Select interest type 
Print out answer 
If selected bond 
Use formula 
Print out answer
"""

# Welcome message and user input prompt for selecting either 'investment' or 'bond'.
print("Investment - Calculate interest earned on investment.")
print("Bond - Calculate monthly bond repayment.")
print(" ")
user_choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

# Investment option
if user_choice == 'investment':
    # Prompt for deposit amount, interest rate, and investment duration.
    deposit_amount = int(input("Please enter the amount you are depositing: "))
    interest_rate = int(input("Please enter the provided interest rate in percentages: "))
    investment_years = int(input("How many years will you be investing? "))
    
    # Prompt for selecting between 'simple' or 'compound' interest.
    simple_compound = input("Would you like 'simple' or 'compound' interest? ")

    # Calculate simple or compound interest based on user choice.
    if simple_compound == "simple":
        simple_interest = deposit_amount * (1 + (interest_rate / 100) * investment_years)
        print(f"Your return is {simple_interest}")
    else:
        import math
        compound_interest = deposit_amount * math.pow((1 + interest_rate / 100), investment_years)
        print(f"Your return is {compound_interest}")

# Bond option
elif user_choice == 'bond':
    print("Thank you!")
    
    # Prompt for house value, monthly interest rate, and repayment duration.
    house_value = int(input("Please enter the present value of the house: "))
    monthly_rate = int(input("Enter your monthly interest rate: "))
    repayment_months = int(input("Enter the number of months to repay the bond: "))   
    
    # Calculate monthly bond repayment.
    repayment = (((monthly_rate / 12) / 100) * house_value) / (1 - (1 + (monthly_rate / 12) / 100) ** (-repayment_months))
    print(f"Your expected monthly repayment is {repayment}.")

# Error message for invalid input
else:
    print("Sorry, you entered invalid data. Please choose from the options above.")
