import math

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))

# if number1 > number2 and number1 > number3:
#     print(f"{number1} is largest")
# elif number2 > number1 and number2 > number3:
#     print(f"{number2} is largest")
# else:
#     print(f"{number3} is largest")

print(f"largest is {max(number1, max(number2,number3))}")

