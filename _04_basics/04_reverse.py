number = int(input("Enter number: "))
reverse = 0

while number != 0:
    last_digit = number % 10
    reverse = reverse*10 + last_digit
    number = number // 10

print(f"Reverse is {reverse}")
