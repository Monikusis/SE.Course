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

# Welcome message
print("Investment - to calculate the amount of interest you'll earn on your investment")
print("Bond - to calculate the amount you'll have to pay on a home loan")
print(" ")
user_choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

# Investment option
if user_choice == 'investment':
    

    deposit_amount = int(input("Please enter the amount you are depositing: "))
    interest_rate = int(input("Please enter your provided interest rate in percentages: "))
    investment_years = int(input("How many years you will be investing? "))  
    
    # 'Simple' or ' Compound' option
    simple_compound = input("Would you like 'simple' or 'compound' interest? ")

    interest = simple_compound
    
    simple_interest =  deposit_amount*(1 + (interest_rate/100)*investment_years)
    compound_interest = deposit_amount * math.pow((1 + interest_rate/100),investment_years)
    
    if simple_interest == "simple":
        print(f"Your return is {simple_interest}")
    else:
        print(f"Your return is {compound_interest}")

#'Bond' option
elif user_choice == 'bond':
    print("Thank you!")

    house_value = int(input("Please present value of the house: "))
    monthly_rate = int(input("Your monthly interest rate: "))
    repayment_months = int(input("The number of months to repay the bond: "))   
    
    repayment = (((monthly_rate/12) / 100) * house_value) / (1 - (1 + (monthly_rate/12) / 100) ** (-repayment_months))
    print(f"Your expected monthly repayment is {repayment}.")
    
# Error message 
else:
    print("Sorry you entered invalid data, please choose from above.")

 
    








 





