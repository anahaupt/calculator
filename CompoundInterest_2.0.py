#This script returns the future value of an investment, calculated using compound interest.

#Arguments
#   presentValue = float(The initial investment value)
#   rate = float(The interest rate according to the period of compounding (i.e. 0.02))
#   numberOfPeriods = int(The number of periods for the investment)

#Return
#   The total amount of the investment.


def futureValue(presentValue, rate, numberOfPeriods):
    return (presentValue * (1+rate)**numberOfPeriods)

print(futureValue(1000, 0.01, 12))