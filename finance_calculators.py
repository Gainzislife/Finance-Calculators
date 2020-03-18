import math

# Print start of application with 2 choices - investment and bond
print("Choose either 'investment' or 'bond' from the menu below to proceed:\n")
selection = input('''investment \t - to calculate the amount of interest you'll earn on interest \nbond \t\t - to calculate the amount you'll have to pay on a home loan\n''')

# Change the input to lowercase
selection = selection.lower()
# Check if input is correct. Continue to calculation if it is
######## Investment ########
if selection == "investment":
    deposit = float(input("The amount of money to deposit? "))
    interest_rate = float(input("The interest in '%'? "))
    years = float(input("Years investing for? "))
    interest = input("'Simple' or 'compound' interest? ")

    # Make interest type input lowercase and divide interest rate by 100
    interest = interest.lower()
    interest_rate = interest_rate / 100

    # Calculate according to chosen interest type
    if interest == "simple":
        total = deposit * (1 + interest_rate * years)
        print("Your total with simple interest is: R " + str(round(total, 2)))
    elif interest == "compound":
        total = deposit * math.pow((1 + interest_rate), years)
        print("Your total with compound interest is: R " + str(round(total, 2)))
    else:
        print("Your input is wrong. Enter 'simple' or 'compound'.")
######## Bond ########
elif selection == "bond":
    house_value = float(input("Value of the house? "))
    interest_rate = float(input("The interest in '%'? "))
    months = float(input("Months until bond is paid? "))

    # Divide interest_rate by 100
    interest_rate = interest_rate / 100
    val = math.pow(1 + interest_rate, months) # variable used to do math.pow calculation only once
    repayment = house_value * ((interest_rate * val) / (val - 1))
    print("Your monthly repayments are: R " + str(round(repayment, 2)))
else:
  print("Your input doesn't make sense, please enter 'investment' or 'bond'.")
