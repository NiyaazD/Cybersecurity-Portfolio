import math

# display menu for investment options

print("Investment - to calculate the amount of interest you'll earn on your investment.")
print("Bond - to calculate the amount you'll have to pay on a home loan.")

# request for the user to select an option of either "Investment" or "Bond"
# convert the user's input to lowercase to make it case-senstive

choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

# if the user chooses "investment" request the below inputs:
#    - the amount of money they are depositing
#    - the interest rate (percentage)
#    - number of years of investment
#    - "simple" or "compound" interest

if choice == "investment":

    deposit = float(input("Enter the amount of money you are depositing: "))
    interest_rate = float(input("Enter the interest rate as a percentage: "))
    years = int(input("Enter the number of years you plan on investing: "))

    interest = input("Do you want 'compound' or 'simple' interest?")

    # if simple interest use formula: A = P * (1 + r * t)
    # if compound interest use formula: A = P * (1 + r) ** t

    # converting percentage to a decimal

    r = interest_rate / 100

    if interest == "simple":
        amount = deposit * (1 + r * years)
        print(f"You will receive R{amount: .2f} after {years} years.")
    
    elif interest == "compound":
        amount = deposit * (1 + r) ** years
        print(f"You will receive R{amount: .2f} after {years} years.")

    else: 
        print("invalid interest type selected.")

# if the user enters "bond" request the below inputs:
#    - the value of the house
#    - the interest rate
#    - the number of months of the repayment term

elif choice == "bond": 

    house_value = float(input("Enter the value of the house: "))
    interest_rate = float(input("Enter the interest rate as a percentage: "))
    payment_term = int(input("Enter the number of months you plan to repay the bond: "))

    # formula to be used to calculate monthly repayment:
    #    - repayment = (i * P) / (1 - (1 + i) ** (-n))

    # monthly interest

    i = (interest_rate / 100) / 12

    repayment = (i * house_value) / (1 - (1 + i) ** (-payment_term))

    print(f"Your monthly repayment will be R{repayment:.2f}.")

else: 
    print("Invalid selection. Please enter either 'investment' or 'bond'.")
