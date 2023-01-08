#This script returns the value of each slice of a loan

presentValue = float(input("Enter the total amount financed:"))
rate = float(input("Enter the interest rate according to the period of compounding (i.e. 0.02)"))
numberOfPeriods = int(input("Enter the number of payment periods:"))

#Loan Payment = ((PV * i * (1+i)ˆn) / ((1+i)ˆn)-1)
loanPayment = ((presentValue * rate * ((1 + rate)**numberOfPeriods)) / (((1 + rate)**numberOfPeriods)-1))

print(loanPayment)