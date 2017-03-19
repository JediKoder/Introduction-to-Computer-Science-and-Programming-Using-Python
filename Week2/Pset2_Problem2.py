# Problem 2 - Paying Debt off in a Year
# program that calculates the minimum fixed monthly payment needed in order pay off a credit card
# balance within 12 months.

# Test Case #1
#balance = 3329
#annualInterestRate = 0.2

# Test Case #2
#balance = 4773
#annualInterestRate = 0.2

# Test Case #3
balance = 3926
annualInterestRate = 0.2

# Global Variables
monthlyInterestRate = annualInterestRate / 12.0
previousBalance = balance
monthlyFixedPayment = 10

# Main Program

while True:

    for month in range(12):
        monthlyUnpaidBalance = previousBalance - monthlyFixedPayment
        previousBalance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)

    if previousBalance > 0:
        monthlyFixedPayment += 10
        previousBalance = balance
    else:
        break

print('Lowest Payment:', monthlyFixedPayment)

