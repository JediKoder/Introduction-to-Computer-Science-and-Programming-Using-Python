# Problem 1 - Paying Debt off in a Year

# Test Case #1
balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

# Test Case #2
#balance = 484
#annualInterestRate = 0.2
#monthlyPaymentRate = 0.04

# Global Variables
monthlyInterestRate = annualInterestRate / 12.0
previousBalance = balance
# Main Program

for month in range(12):
    minimumMonthlyPayment = monthlyPaymentRate * previousBalance
    monthlyUnpaidBalance = previousBalance - minimumMonthlyPayment
    previousBalance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)

print('Remaining balance:', round(previousBalance, 2))

