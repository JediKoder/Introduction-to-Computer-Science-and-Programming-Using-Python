# Problem 3 - Paying Debt off in a Year
# program that calculates the minimum fixed monthly payment needed in order pay off a credit card
# balance within 12 months.
# Using Binary Search

# Test Case #1
balance = 320000
annualInterestRate = 0.2

# Test Case #2
#balance = 4773
#annualInterestRate = 0.2

# Test Case #3
#balance = 3926
#annualInterestRate = 0.2

# Global Variables
monthlyInterestRate = annualInterestRate / 12.0
monthlyPaymentLower = round(balance / 12, 2)
monthlyPaymentUpper = round((balance * (1 + monthlyInterestRate)**12) / 12.0, 2)
previousBalance = balance
monthlyFixedPayment = round((monthlyPaymentUpper + monthlyPaymentLower) / 2, 2)

# Main Program


while True:

    for month in range(12):
        monthlyUnpaidBalance = round(previousBalance - monthlyFixedPayment, 2)
        previousBalance = round(monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance), 2)

    if previousBalance < 0.1 and previousBalance > -0.1:
        break

    elif previousBalance < 0:
        monthlyPaymentUpper = round(monthlyFixedPayment, 2)

    elif previousBalance > 0:
        monthlyPaymentLower = round(monthlyFixedPayment, 2)

    previousBalance = balance
    monthlyFixedPayment = round((monthlyPaymentUpper + monthlyPaymentLower) / 2, 2)

print('Lowest Payment:', monthlyFixedPayment)

