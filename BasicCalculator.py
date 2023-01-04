#This is a calculator script with basic functions

operator = input ("Type the math operation you would like to complete:")

number1 = float(input("Enter your first number:"))
number2 = float(input("Enter your second number:"))

if operator == "+":
    answer = number1 + number2
    print("{} + {} = {}".format(number1, number2, answer)) 

elif operator == "-":
    answer = number1 - number2
    print("{} - {} = {}".format(number1, number2, answer))

elif operator == "*":
    answer = number1 * number2
    print("{} * {} = {}".format(number1, number2, answer))

elif operator == "/":
    answer = number1 / number2
    print("{} / {} = {}".format(number1, number2, answer))

elif operator == "ˆ" or operator == "**":
    answer = number1 ** number2
    print("{} ˆ {} = {}".format(number1, number2, answer))

else:
    print("Please restart and insert a valid operator")