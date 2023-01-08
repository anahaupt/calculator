#This script returns the future value of an investment, calculated using compound interest.

presentValue = float((input("Enter the initial investment value:")))
rate = float(input("Enter the interest rate according to the period of compounding (i.e. 0.02):"))
numberOfPeriods = int(input("Enter the number of periods for the investment:"))

futureValue = presentValue * (1 + rate) ** numberOfPeriods

print(futureValue)